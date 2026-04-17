import struct


class BinaryReader:
    """Helper to read big‑endian data from a bytes object.

    Instances maintain a cursor into an internal buffer.  Note that all
    multibyte values in the BPSR protocol are big‑endian.
    """

    def __init__(self, data: bytes):
        self._buffer = memoryview(data)
        self._pos = 0

    def remaining(self) -> int:
        return len(self._buffer) - self._pos

    def read(self, length: int) -> bytes:
        if self._pos + length > len(self._buffer):
            raise EOFError("unexpected end of buffer")
        b = self._buffer[self._pos: self._pos + length].tobytes()
        self._pos += length
        return b

    def peek_u32(self) -> int:
        if self.remaining() < 4:
            raise EOFError
        return struct.unpack_from(">I", self._buffer, self._pos)[0]

    def read_u16(self) -> int:
        return struct.unpack(">H", self.read(2))[0]

    def read_u32(self) -> int:
        return struct.unpack(">I", self.read(4))[0]

    def read_u64(self) -> int:
        return struct.unpack(">Q", self.read(8))[0]

    def read_remaining(self) -> bytes:
        return self.read(self.remaining())


class TCPReassembler:
    """Simple TCP stream reassembler.

    Maintains an ordered map of sequence numbers to payloads and yields
    contiguous data when possible.  Only one stream is tracked at a time,
    matching the behaviour of the Rust code where the game server is
    identified and then the sniffer begins reassembling that connection.
    """

    def __init__(self) -> None:
        self.cache: dict[int, bytes] = {}  # seq_num -> payload
        self.next_seq: int | None = None
        self._data = bytearray()

    def clear(self, seq: int) -> None:
        self.cache.clear()
        self.next_seq = seq
        self._data.clear()

    def push(self, seq: int, payload: bytes) -> None:
        if not payload:
            return
        self.cache.setdefault(seq, payload)
        # establish the next expected sequence if unknown
        if self.next_seq is None:
            self.next_seq = seq
        # buffer contiguous segments
        while self.next_seq in self.cache:
            seg = self.cache.pop(self.next_seq)
            self._data.extend(seg)
            self.next_seq = (self.next_seq + len(seg)) & 0xFFFFFFFF

    def pop_frames(self) -> list[bytes]:
        """Extract complete length‑prefixed frames from the buffered data.

        The BPSR protocol prefixes each frame with a 32‑bit big‑endian
        length.  If not enough data is available for a complete frame
        nothing is returned.
        """
        frames: list[bytes] = []
        while len(self._data) >= 4:
            frame_len = struct.unpack(">I", self._data[:4])[0]
            if len(self._data) < frame_len:
                break
            # slice out the complete frame and remove it from buffer
            frame = bytes(self._data[:frame_len])
            del self._data[:frame_len]
            frames.append(frame)
        return frames
