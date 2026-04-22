import logging
from dataclasses import dataclass
from enum import Enum
from typing import Iterator, Optional

import zstandard as zstd  # Optional, used for compressed fragments
from google.protobuf.message import Message

from star_resonance_relay.proto.serv_chit_chat_ntf_pb2 import ChitChatNtf
from star_resonance_relay.proto.serv_world_ntf_pb2 import WorldNtf
from star_resonance_relay.utils import BinaryReader

logger = logging.getLogger(__name__)


class FragmentType(Enum):
    """Enumeration of fragment types used within the BPSR protocol."""

    NONE = 0
    CALL = 1
    NOTIFY = 2
    RETURN = 3
    ECHO = 4
    FRAME_UP = 5
    FRAME_DOWN = 6


@dataclass(slots=True, frozen=True)
class NotifyFrame:
    """Decoded Notify frame contents.

    Represents a single Notify frame extracted from BPSR network traffic.
    Contains the essential metadata and payload data needed for further
    processing by higher-level decoders.

    Attributes:
        service_uid: Unique identifier for the service (typically 0x63335342).
        stub_id: Stub identifier for the RPC call.
        method_id: Method identifier indicating the type of message.
        payload: Raw binary payload data (may be decompressed).
        was_compressed: Whether the payload was decompressed from zstd.
        offset: Byte offset where this frame was found in the original data.

    Example:
        >>> frame = NotifyFrame(0x63335342, 123, 0x2E, b'data', False)
        >>> print(f"Method: 0x{frame.method_id:08x}")
        Method: 0x0000002E
    """

    service_uid: int
    stub_id: int
    method_id: int
    payload: bytes
    was_compressed: bool


class BPSRPacketProcessor:
    """Process assembled BPSR frames into method opcodes and payloads.
    """

    def __init__(self) -> None:
        # optional mapping of opcodes to protobuf decoders
        self.proto_map: dict[int, dict[int, type[Message]]] = {
            0x0000000063335342: {
                0x00000006: WorldNtf.SyncNearEntities,
                0x00000015: WorldNtf.SyncContainerData,
                0x00000016: WorldNtf.SyncContainerDirtyData,
                0x0000002E: WorldNtf.SyncToMeDeltaInfo,
                0x0000002D: WorldNtf.SyncNearDeltaInfo
            },
            0x0000000009d4a768: {
                0x00000001: ChitChatNtf.NotifyNewestChitChatMsgs
            }
        }
        # Reuse a single decompressor instance to avoid per-packet allocation
        self._dctx = zstd.ZstdDecompressor() if zstd else None

    def _parse_notify(self, body: bytes, is_zstd: bool) -> NotifyFrame | None:
        """Parse a Notify frame body into a NotifyFrame object.

        Extracts the service UID, stub ID, method ID, and payload from a
        Notify frame body. Handles decompression if the frame was marked
        as compressed.

        Args:
            body: Raw frame body data.
            is_zstd: Whether the payload is compressed with zstd.

        Returns:
            NotifyFrame | None: Parsed frame object, or None if parsing fails.
        """
        # Notify frames must have at least 16 bytes (service_uid + stub_id + method_id)
        if len(body) < 16:
            return None

        # Extract header fields (all big-endian)
        reader = BinaryReader(body)

        service_uid = reader.read_u64()
        stub_id = reader.read_u32()
        method_id = reader.read_u32()
        payload = reader.read_remaining()
        dctx = self._dctx

        # Decompress payload if needed (decompressor is passed in to avoid re-allocation)
        if is_zstd and dctx is not None:
            try:
                payload = dctx.decompress(payload, max_output_size=1024*1024)
            except Exception as e:
                logger.debug(f"Decompression failed in _parse_notify: {e}")
                return None

        return NotifyFrame(
            service_uid=service_uid,
            stub_id=stub_id,
            method_id=method_id,
            payload=payload,
            was_compressed=is_zstd
        )

    def process_frame(self, frame: bytes) -> Iterator[NotifyFrame]:
        """Yield NotifyFrame from a single BPSR frame."""
        reader = BinaryReader(frame)
        while reader.remaining() > 0:
            try:
                pkt_len = reader.peek_u32()
            except EOFError:
                break
            if pkt_len < 6 or reader.remaining() < pkt_len:
                # malformed or incomplete
                break

            fragment = BinaryReader(reader.read(pkt_len))

            # skip length field
            fragment.read_u32()
            frag_type_field = fragment.read_u16()

            is_compressed = bool(frag_type_field & 0x8000)
            try:
                frag_type = FragmentType(frag_type_field & 0x7FFF)
            except ValueError:
                continue

            match frag_type:
                case FragmentType.NOTIFY:
                    result = self._parse_notify(fragment.read_remaining(), is_compressed)
                    if result is not None:
                        yield result
                case FragmentType.FRAME_DOWN:
                    # nested frame; read server sequence id and recurse
                    _server_seq = fragment.read_u32()
                    nested = fragment.read_remaining()
                    if is_compressed and self._dctx is not None:
                        try:
                            nested = self._dctx.decompress(nested, max_output_size=1024*1024)
                        except Exception:
                            continue
                    # Recursively process nested frames
                    for tup in self.process_frame(nested):
                        yield tup
                case _:
                    # other fragment types are ignored for now
                    pass

    def process_bytes(self, data: bytes) -> Iterator[NotifyFrame]:
        """Process one or more concatenated BPSR frames from a byte string."""
        frames = []
        reader = BinaryReader(data)
        while reader.remaining() >= 4:
            try:
                frame_len = reader.peek_u32()
            except EOFError:
                break
            if frame_len == 0 or reader.remaining() < frame_len:
                break
            frames.append(reader.read(frame_len))
        for frame in frames:
            yield from self.process_frame(frame)

    def decode_payload(self, frame: NotifyFrame) -> Optional[Message]:
        """Decode a raw payload into a protobuf message if possible.

        Returns None if the frame's service/method is not registered or
        decoding fails, instead of raising an exception.
        """
        method_map = self.proto_map.get(frame.service_uid)
        if method_map is None:
            return None

        decoder = method_map.get(frame.method_id)
        if decoder is None:
            return None

        try:
            # All compiled protobuf messages support ``FromString``
            return decoder.FromString(frame.payload)  # type: ignore[attr-defined]
        except Exception as exc:  # pragma: no cover
            logger.warning("Failed to decode %s: %s", frame, exc)
            return None
