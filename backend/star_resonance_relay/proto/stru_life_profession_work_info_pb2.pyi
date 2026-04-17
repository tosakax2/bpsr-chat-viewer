import stru_item_pb2 as _stru_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LifeProfessionWorkInfo(_message.Message):
    __slots__ = ("life_profession_id", "begin_time", "end_time", "count", "cost", "reward", "cost_id")
    LIFE_PROFESSION_ID_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    REWARD_FIELD_NUMBER: _ClassVar[int]
    COST_ID_FIELD_NUMBER: _ClassVar[int]
    life_profession_id: int
    begin_time: int
    end_time: int
    count: int
    cost: int
    reward: _containers.RepeatedCompositeFieldContainer[_stru_item_pb2.Item]
    cost_id: int
    def __init__(self, life_profession_id: _Optional[int] = ..., begin_time: _Optional[int] = ..., end_time: _Optional[int] = ..., count: _Optional[int] = ..., cost: _Optional[int] = ..., reward: _Optional[_Iterable[_Union[_stru_item_pb2.Item, _Mapping]]] = ..., cost_id: _Optional[int] = ...) -> None: ...
