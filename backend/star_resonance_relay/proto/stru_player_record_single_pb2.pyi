from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerRecordSingle(_message.Message):
    __slots__ = ("id", "total_count", "cycle_count", "cycle_time")
    ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CYCLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CYCLE_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    total_count: int
    cycle_count: int
    cycle_time: int
    def __init__(self, id: _Optional[int] = ..., total_count: _Optional[int] = ..., cycle_count: _Optional[int] = ..., cycle_time: _Optional[int] = ...) -> None: ...
