from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ItemCounterInfo(_message.Message):
    __slots__ = ("id", "counter", "accumulate_limit", "end_time")
    ID_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    ACCUMULATE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    counter: int
    accumulate_limit: int
    end_time: int
    def __init__(self, id: _Optional[int] = ..., counter: _Optional[int] = ..., accumulate_limit: _Optional[int] = ..., end_time: _Optional[int] = ...) -> None: ...
