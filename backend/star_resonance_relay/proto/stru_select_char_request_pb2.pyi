from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SelectCharRequest(_message.Message):
    __slots__ = ("token", "char_id", "area_id")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    AREA_ID_FIELD_NUMBER: _ClassVar[int]
    token: str
    char_id: int
    area_id: int
    def __init__(self, token: _Optional[str] = ..., char_id: _Optional[int] = ..., area_id: _Optional[int] = ...) -> None: ...
