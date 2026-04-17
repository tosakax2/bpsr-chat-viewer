import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MaterialShowDataTableBase(_message.Message):
    __slots__ = ("id", "start", "duration", "end", "is_attacker", "state_id", "group_id", "material_type", "colour", "power", "colour_curve", "power_curve", "colour2", "power2", "is_body", "is_primary_weapon", "is_secondary_weapon")
    ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    IS_ATTACKER_FIELD_NUMBER: _ClassVar[int]
    STATE_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    COLOUR_FIELD_NUMBER: _ClassVar[int]
    POWER_FIELD_NUMBER: _ClassVar[int]
    COLOUR_CURVE_FIELD_NUMBER: _ClassVar[int]
    POWER_CURVE_FIELD_NUMBER: _ClassVar[int]
    COLOUR2_FIELD_NUMBER: _ClassVar[int]
    POWER2_FIELD_NUMBER: _ClassVar[int]
    IS_BODY_FIELD_NUMBER: _ClassVar[int]
    IS_PRIMARY_WEAPON_FIELD_NUMBER: _ClassVar[int]
    IS_SECONDARY_WEAPON_FIELD_NUMBER: _ClassVar[int]
    id: int
    start: float
    duration: float
    end: float
    is_attacker: bool
    state_id: int
    group_id: int
    material_type: int
    colour: _table_basic_pb2.number_array
    power: float
    colour_curve: _table_basic_pb2.number_table
    power_curve: _table_basic_pb2.number_table
    colour2: _table_basic_pb2.number_array
    power2: float
    is_body: bool
    is_primary_weapon: bool
    is_secondary_weapon: bool
    def __init__(self, id: _Optional[int] = ..., start: _Optional[float] = ..., duration: _Optional[float] = ..., end: _Optional[float] = ..., is_attacker: bool = ..., state_id: _Optional[int] = ..., group_id: _Optional[int] = ..., material_type: _Optional[int] = ..., colour: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., power: _Optional[float] = ..., colour_curve: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., power_curve: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., colour2: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., power2: _Optional[float] = ..., is_body: bool = ..., is_primary_weapon: bool = ..., is_secondary_weapon: bool = ...) -> None: ...

class MaterialShowDataTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MaterialShowDataTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MaterialShowDataTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MaterialShowDataTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MaterialShowDataTableBase]] = ...) -> None: ...
