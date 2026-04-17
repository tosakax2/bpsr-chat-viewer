from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlaceHolderPlayer(_message.Message):
    __slots__ = ("char_id", "name")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    name: str
    def __init__(self, char_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
