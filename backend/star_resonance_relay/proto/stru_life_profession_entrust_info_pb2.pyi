from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LifeProfessionEntrustInfo(_message.Message):
    __slots__ = ("life_profession_id", "begin_time", "end_time", "base_id", "count", "cost_id", "cost")
    LIFE_PROFESSION_ID_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    BASE_ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    COST_ID_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    life_profession_id: int
    begin_time: int
    end_time: int
    base_id: int
    count: int
    cost_id: int
    cost: int
    def __init__(self, life_profession_id: _Optional[int] = ..., begin_time: _Optional[int] = ..., end_time: _Optional[int] = ..., base_id: _Optional[int] = ..., count: _Optional[int] = ..., cost_id: _Optional[int] = ..., cost: _Optional[int] = ...) -> None: ...
