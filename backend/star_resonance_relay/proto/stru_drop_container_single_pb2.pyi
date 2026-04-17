from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DropContainerSingle(_message.Message):
    __slots__ = ("id", "count", "cycle_time", "history_count")
    ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    CYCLE_TIME_FIELD_NUMBER: _ClassVar[int]
    HISTORY_COUNT_FIELD_NUMBER: _ClassVar[int]
    id: int
    count: int
    cycle_time: int
    history_count: int
    def __init__(self, id: _Optional[int] = ..., count: _Optional[int] = ..., cycle_time: _Optional[int] = ..., history_count: _Optional[int] = ...) -> None: ...
