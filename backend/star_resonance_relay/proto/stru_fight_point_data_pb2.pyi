import stru_fight_point_sub_data_pb2 as _stru_fight_point_sub_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FightPointData(_message.Message):
    __slots__ = ("function_type", "total_point", "point", "sub_function_data")
    class SubFunctionDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_fight_point_sub_data_pb2.FightPointSubData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_fight_point_sub_data_pb2.FightPointSubData, _Mapping]] = ...) -> None: ...
    FUNCTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_POINT_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    SUB_FUNCTION_DATA_FIELD_NUMBER: _ClassVar[int]
    function_type: int
    total_point: int
    point: int
    sub_function_data: _containers.MessageMap[int, _stru_fight_point_sub_data_pb2.FightPointSubData]
    def __init__(self, function_type: _Optional[int] = ..., total_point: _Optional[int] = ..., point: _Optional[int] = ..., sub_function_data: _Optional[_Mapping[int, _stru_fight_point_sub_data_pb2.FightPointSubData]] = ...) -> None: ...
