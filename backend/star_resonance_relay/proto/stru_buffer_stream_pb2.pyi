from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BufferStream(_message.Message):
    __slots__ = ("Buffer",)
    BUFFER_FIELD_NUMBER: _ClassVar[int]
    Buffer: bytes
    def __init__(self, Buffer: _Optional[bytes] = ...) -> None: ...
