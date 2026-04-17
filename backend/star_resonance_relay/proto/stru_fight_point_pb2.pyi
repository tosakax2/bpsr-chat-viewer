import stru_fight_point_data_pb2 as _stru_fight_point_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FightPoint(_message.Message):
    __slots__ = ("total_fight_point", "fight_point_data")
    class FightPointDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_fight_point_data_pb2.FightPointData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_fight_point_data_pb2.FightPointData, _Mapping]] = ...) -> None: ...
    TOTAL_FIGHT_POINT_FIELD_NUMBER: _ClassVar[int]
    FIGHT_POINT_DATA_FIELD_NUMBER: _ClassVar[int]
    total_fight_point: int
    fight_point_data: _containers.MessageMap[int, _stru_fight_point_data_pb2.FightPointData]
    def __init__(self, total_fight_point: _Optional[int] = ..., fight_point_data: _Optional[_Mapping[int, _stru_fight_point_data_pb2.FightPointData]] = ...) -> None: ...
