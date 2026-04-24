import logging
import queue
import threading
from dataclasses import dataclass
from typing import Self, override, Callable

from google.protobuf.message import Message
from scapy.layers.inet import TCP, IP
from scapy.packet import Packet, Raw
from scapy.config import conf
conf.layers.filter([TCP, IP])

from star_resonance_relay.processor import BPSRPacketProcessor
from star_resonance_relay.utils import TCPReassembler, BinaryReader

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class ServerPort:
    ip: str
    port: int


@dataclass(frozen=True, slots=True)
class Endpoints:
    source: ServerPort
    destination: ServerPort

    @classmethod
    def from_packet(cls, packet: Packet) -> Self:
        return cls(
            ServerPort(packet[IP].src, packet[TCP].sport),
            ServerPort(packet[IP].dst, packet[TCP].dport)
        )


class Sniffer:
    # Maximum number of raw payloads buffered between sniffer and worker.
    # If the worker falls behind, older packets are dropped rather than
    # blocking the sniffer thread (and by extension the Npcap driver).
    _QUEUE_MAXSIZE = 256

    def __init__(self, callback: Callable[[Message], None]):
        self._callback = callback
        self._known_server: Endpoints | None = None
        self._processor = BPSRPacketProcessor()
        # Queue that decouples packet reception from packet processing.
        # The sniffer thread only enqueues raw bytes; the worker thread does
        # all the heavy lifting (frame parsing, protobuf decoding, broadcast).
        self._pkt_queue: queue.Queue[bytes | None] = queue.Queue(maxsize=self._QUEUE_MAXSIZE)
        # Start the worker thread immediately so it is ready when packets arrive.
        self._worker_thread = threading.Thread(
            target=self._worker,
            name="sniffer-worker",
            daemon=True
        )
        self._worker_thread.start()

    def _is_server(self, payload: bytes) -> bool:
        raise NotImplementedError

    # ------------------------------------------------------------------
    # Sniffer thread — keep this as short as possible
    # ------------------------------------------------------------------
    def handle_packet(self, packet: Packet) -> None:
        """Called by scapy for every captured packet.

        The goal here is to return to the Npcap driver as quickly as
        possible.  We only extract the raw bytes and the endpoint pair,
        do the cheap server-discovery check, and then hand work off to
        the worker thread via a non-blocking queue put.
        """
        if TCP not in packet or IP not in packet or Raw not in packet:
            return

        try:
            tcp_payload = bytes(packet[Raw])
            endpoints = Endpoints.from_packet(packet)

            # 1) Server discovery — cheap byte comparison, done on sniffer thread
            if self._known_server != endpoints:
                if self._is_server(tcp_payload):
                    logger.info(f"Locking to flow {endpoints.source} <-> {endpoints.destination}")
                    self._known_server = endpoints
                else:
                    return  # unknown flow, skip

            # 2) Enqueue raw bytes for the worker thread — non-blocking
            try:
                self._pkt_queue.put_nowait(tcp_payload)
            except queue.Full:
                # Drop the oldest item and enqueue the new one to keep latency low
                try:
                    self._pkt_queue.get_nowait()
                except queue.Empty:
                    pass
                try:
                    self._pkt_queue.put_nowait(tcp_payload)
                except queue.Full:
                    pass
        except Exception:
            logger.exception("handle_packet error")

    # ------------------------------------------------------------------
    # Worker thread — does all the heavy processing
    # ------------------------------------------------------------------
    def _worker(self) -> None:
        """Consume raw payloads from the queue and decode them.

        Runs in a dedicated daemon thread so that all CPU-intensive work
        (frame parsing, zstd decompression, protobuf decoding) is isolated
        from the Npcap driver callback thread.
        """
        while True:
            try:
                tcp_payload = self._pkt_queue.get(timeout=1)
            except queue.Empty:
                continue

            # None is the sentinel value used to stop the worker
            if tcp_payload is None:
                break

            try:
                for frame in self._processor.process_frame(tcp_payload):
                    logger.debug(f"Found {frame}")
                    message = self._processor.decode_payload(frame)
                    if message is None:
                        continue
                    self._callback(message)
            except Exception:
                logger.exception("worker processing error")
            finally:
                self._pkt_queue.task_done()


class BPSRDefaultSniffer(Sniffer):
    SIGNATURE = b"\x00\x63\x33\x53\x42\x00"  # 00 63 33 53 42 00
    SIGNATURE1 = b"\x00\x00\x00\x62\x00\x03\x00\x00\x00\x01"
    SIGNATURE2 = b"\x00\x00\x00\x00\x0a\x4e"

    def _is_scene_change(self, payload: bytes) -> bool:
        """Check if a small packet contains the magic signature used to find
        the game server during scene changes.
        """
        # 5th byte (index 4) must be zero
        if len(payload) < 10 or payload[4] != 0:
            return False
        reader = BinaryReader(payload[10:])
        # Walk through fragments within the TCP payload looking for the
        # signature at offset 5 of the fragment.
        while reader.remaining() >= 4:
            frag_len = reader.read_u32()
            frag_len_minus_hdr = frag_len - 4
            if reader.remaining() < frag_len_minus_hdr:
                break
            frag = reader.read(frag_len_minus_hdr)
            if len(frag) >= 5 + len(self.SIGNATURE):
                if frag[5: 5 + len(self.SIGNATURE)] == self.SIGNATURE:
                    return True
        return False

    def _is_login_packet(self, payload: bytes) -> bool:
        """Detect a login response packet based on fixed signatures.

        When the user first logs in the server’s address can be
        discovered by looking for a payload length of 98 bytes along
        with two fixed signatures in the header.
        """
        return (
                len(payload) == 98
                and payload.startswith(self.SIGNATURE1)
                and payload[14:20] == self.SIGNATURE2
        )

    @override
    def _is_server(self, payload: bytes) -> bool:
        return self._is_scene_change(payload) or self._is_login_packet(payload)


class BPSRChatSniffer(Sniffer):
    SIGNATURE = bytes.fromhex("0000009a00020000000004a84519")
    SIGNATURE_2 = bytes.fromhex("00020000000009d4a768")

    @override
    def _is_server(self, payload: bytes) -> bool:
        length = len(payload)
        # SIGNATURE is 14 bytes; quick length check first
        if length < len(self.SIGNATURE):
            return False
        if payload[:len(self.SIGNATURE)] == self.SIGNATURE:
            return True
        # Limit SIGNATURE_2 scan to the first 256 bytes to avoid full-payload scan
        return self.SIGNATURE_2 in payload[:256]
