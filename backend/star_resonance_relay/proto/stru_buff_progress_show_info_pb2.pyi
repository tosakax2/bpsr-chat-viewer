from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BuffProgressShowInfo(_message.Message):
    __slots__ = ("is_close", "last", "value", "speed", "change_value", "is_only_self")
    IS_CLOSE_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    CHANGE_VALUE_FIELD_NUMBER: _ClassVar[int]
    IS_ONLY_SELF_FIELD_NUMBER: _ClassVar[int]
    is_close: bool
    last: int
    value: int
    speed: float
    change_value: int
    is_only_self: bool
    def __init__(self, is_close: bool = ..., last: _Optional[int] = ..., value: _Optional[int] = ..., speed: _Optional[float] = ..., change_value: _Optional[int] = ..., is_only_self: bool = ...) -> None: ...
