import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MonsterFightAreaTableBase(_message.Message):
    __slots__ = ("id", "area_name", "area_hate_weight", "area_radius", "area_maximum_radius", "area_angle", "player_hate_weight")
    ID_FIELD_NUMBER: _ClassVar[int]
    AREA_NAME_FIELD_NUMBER: _ClassVar[int]
    AREA_HATE_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    AREA_RADIUS_FIELD_NUMBER: _ClassVar[int]
    AREA_MAXIMUM_RADIUS_FIELD_NUMBER: _ClassVar[int]
    AREA_ANGLE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_HATE_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    id: int
    area_name: _table_basic_pb2.string_array
    area_hate_weight: _table_basic_pb2.int_array
    area_radius: _table_basic_pb2.number_table
    area_maximum_radius: float
    area_angle: _table_basic_pb2.number_table
    player_hate_weight: float
    def __init__(self, id: _Optional[int] = ..., area_name: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., area_hate_weight: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., area_radius: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., area_maximum_radius: _Optional[float] = ..., area_angle: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., player_hate_weight: _Optional[float] = ...) -> None: ...

class MonsterFightAreaTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MonsterFightAreaTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MonsterFightAreaTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MonsterFightAreaTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MonsterFightAreaTableBase]] = ...) -> None: ...
