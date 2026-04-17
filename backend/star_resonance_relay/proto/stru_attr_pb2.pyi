from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Attr(_message.Message):
    __slots__ = ("Id", "RawData")
    ID_FIELD_NUMBER: _ClassVar[int]
    RAWDATA_FIELD_NUMBER: _ClassVar[int]
    Id: int
    RawData: bytes
    def __init__(self, Id: _Optional[int] = ..., RawData: _Optional[bytes] = ...) -> None: ...
