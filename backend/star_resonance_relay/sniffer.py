import logging
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
    def __init__(self, callback: Callable[[Message], None]):
        self._callback = callback
        self._known_server: Endpoints | None = None
        # self._reassembler = TCPReassembler()
        self._processor = BPSRPacketProcessor()

    def _is_server(self, payload: bytes) -> bool:
        raise NotImplementedError

    def handle_packet(self, packet: Packet) -> None:
        if TCP not in packet or IP not in packet or Raw not in packet:
            return

        try:
            tcp_payload = bytes(packet[Raw])
            # tcp_seq = packet[TCP].seq
            endpoints = Endpoints.from_packet(packet)
            # del packet

            # 1) Discover/lock server flow
            if self._known_server != endpoints:
                if self._is_server(tcp_payload):
                    logger.info(f"Locking to flow {endpoints.source} <-> {endpoints.destination}")
                    self._known_server = endpoints
                    # Reset reassembler from next expected seq
                    # Use TCP header's sequence number; pydivert exposes it as packet.tcp.seq_num
                    # self._reassembler.clear(tcp_seq + len(tcp_payload))
                else:
                    return  # don’t process the discovery packet’s payload again

            # 2) Reassemble by TCP sequence number & parse frames for the locked flow
            logger.debug(f"Reading {packet}")
            # self._reassembler.push(tcp_seq, tcp_payload)
            # for frame in self._reassembler.pop_frames():
            for frame in self._processor.process_frame(tcp_payload):
                logger.debug(f"Found {frame}")
                try:
                    message = self._processor.decode_payload(frame)
                except NotImplementedError:
                    continue
                self._callback(message)
        except Exception:
            logger.exception(packet)


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
        return payload.startswith(self.SIGNATURE) or self.SIGNATURE_2 in payload
