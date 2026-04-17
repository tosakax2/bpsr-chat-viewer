from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EnergyItemInfo(_message.Message):
    __slots__ = ("queue_id", "column_id", "refine_state", "gain_time")
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
    REFINE_STATE_FIELD_NUMBER: _ClassVar[int]
    GAIN_TIME_FIELD_NUMBER: _ClassVar[int]
    queue_id: int
    column_id: int
    refine_state: int
    gain_time: int
    def __init__(self, queue_id: _Optional[int] = ..., column_id: _Optional[int] = ..., refine_state: _Optional[int] = ..., gain_time: _Optional[int] = ...) -> None: ...
