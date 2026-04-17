import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DamageAttrTableBase(_message.Message):
    __slots__ = ("id", "level", "name", "damage_type", "type_enum", "damage_script", "pve_damage_radio", "pve_fixed_parameter", "pve_loop_time", "pve_stunned_damage", "pve_extinction_damage", "part_damage_radio", "abnormal_damage", "damage_property", "part_damage_type", "damage_weight", "tags", "behit_light_is_open")
    ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DAMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_ENUM_FIELD_NUMBER: _ClassVar[int]
    DAMAGE_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    PVE_DAMAGE_RADIO_FIELD_NUMBER: _ClassVar[int]
    PVE_FIXED_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    PVE_LOOP_TIME_FIELD_NUMBER: _ClassVar[int]
    PVE_STUNNED_DAMAGE_FIELD_NUMBER: _ClassVar[int]
    PVE_EXTINCTION_DAMAGE_FIELD_NUMBER: _ClassVar[int]
    PART_DAMAGE_RADIO_FIELD_NUMBER: _ClassVar[int]
    ABNORMAL_DAMAGE_FIELD_NUMBER: _ClassVar[int]
    DAMAGE_PROPERTY_FIELD_NUMBER: _ClassVar[int]
    PART_DAMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DAMAGE_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    BEHIT_LIGHT_IS_OPEN_FIELD_NUMBER: _ClassVar[int]
    id: int
    level: int
    name: str
    damage_type: int
    type_enum: int
    damage_script: str
    pve_damage_radio: _table_basic_pb2.int_array
    pve_fixed_parameter: _table_basic_pb2.int_array
    pve_loop_time: int
    pve_stunned_damage: _table_basic_pb2.int_array
    pve_extinction_damage: int
    part_damage_radio: _table_basic_pb2.int_array
    abnormal_damage: _table_basic_pb2.int_table
    damage_property: int
    part_damage_type: int
    damage_weight: _table_basic_pb2.number_array
    tags: _table_basic_pb2.int_array
    behit_light_is_open: bool
    def __init__(self, id: _Optional[int] = ..., level: _Optional[int] = ..., name: _Optional[str] = ..., damage_type: _Optional[int] = ..., type_enum: _Optional[int] = ..., damage_script: _Optional[str] = ..., pve_damage_radio: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., pve_fixed_parameter: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., pve_loop_time: _Optional[int] = ..., pve_stunned_damage: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., pve_extinction_damage: _Optional[int] = ..., part_damage_radio: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., abnormal_damage: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., damage_property: _Optional[int] = ..., part_damage_type: _Optional[int] = ..., damage_weight: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., tags: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., behit_light_is_open: bool = ...) -> None: ...

class DamageAttrTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: DamageAttrTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[DamageAttrTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, DamageAttrTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, DamageAttrTableBase]] = ...) -> None: ...
