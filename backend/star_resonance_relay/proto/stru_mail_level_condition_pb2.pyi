from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MailLevelCondition(_message.Message):
    __slots__ = ("min", "max", "include_level_up")
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LEVEL_UP_FIELD_NUMBER: _ClassVar[int]
    min: int
    max: int
    include_level_up: bool
    def __init__(self, min: _Optional[int] = ..., max: _Optional[int] = ..., include_level_up: bool = ...) -> None: ...
