from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonEnterCount(_message.Message):
    __slots__ = ("enter_time", "enter_count")
    ENTER_TIME_FIELD_NUMBER: _ClassVar[int]
    ENTER_COUNT_FIELD_NUMBER: _ClassVar[int]
    enter_time: int
    enter_count: int
    def __init__(self, enter_time: _Optional[int] = ..., enter_count: _Optional[int] = ...) -> None: ...
