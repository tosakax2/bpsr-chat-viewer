from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetRemindRequest(_message.Message):
    __slots__ = ("char_id", "is_remind")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    IS_REMIND_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    is_remind: bool
    def __init__(self, char_id: _Optional[int] = ..., is_remind: bool = ...) -> None: ...
