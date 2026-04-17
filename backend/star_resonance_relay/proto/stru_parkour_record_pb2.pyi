from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ParkourRecord(_message.Message):
    __slots__ = ("time", "state", "perfect_time")
    TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PERFECT_TIME_FIELD_NUMBER: _ClassVar[int]
    time: int
    state: int
    perfect_time: int
    def __init__(self, time: _Optional[int] = ..., state: _Optional[int] = ..., perfect_time: _Optional[int] = ...) -> None: ...
