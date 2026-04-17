from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetTopRequest(_message.Message):
    __slots__ = ("char_id", "is_top")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    IS_TOP_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    is_top: bool
    def __init__(self, char_id: _Optional[int] = ..., is_top: bool = ...) -> None: ...
