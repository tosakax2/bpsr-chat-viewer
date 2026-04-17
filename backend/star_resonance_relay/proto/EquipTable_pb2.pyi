import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EquipTableBase(_message.Message):
    __slots__ = ("id", "model", "suit_id", "suit_part_id", "equip_part", "equip_type", "type_attr_lib_id", "style_effect_lib_id", "max_durability", "durability_invalid_type", "fashion_m_id", "fashion_f_id", "bonus_grow_times", "basic_grow_range")
    ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SUIT_ID_FIELD_NUMBER: _ClassVar[int]
    SUIT_PART_ID_FIELD_NUMBER: _ClassVar[int]
    EQUIP_PART_FIELD_NUMBER: _ClassVar[int]
    EQUIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_ATTR_LIB_ID_FIELD_NUMBER: _ClassVar[int]
    STYLE_EFFECT_LIB_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_DURABILITY_FIELD_NUMBER: _ClassVar[int]
    DURABILITY_INVALID_TYPE_FIELD_NUMBER: _ClassVar[int]
    FASHION_M_ID_FIELD_NUMBER: _ClassVar[int]
    FASHION_F_ID_FIELD_NUMBER: _ClassVar[int]
    BONUS_GROW_TIMES_FIELD_NUMBER: _ClassVar[int]
    BASIC_GROW_RANGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    model: str
    suit_id: int
    suit_part_id: int
    equip_part: int
    equip_type: int
    type_attr_lib_id: int
    style_effect_lib_id: int
    max_durability: int
    durability_invalid_type: int
    fashion_m_id: int
    fashion_f_id: int
    bonus_grow_times: _table_basic_pb2.int_table
    basic_grow_range: int
    def __init__(self, id: _Optional[int] = ..., model: _Optional[str] = ..., suit_id: _Optional[int] = ..., suit_part_id: _Optional[int] = ..., equip_part: _Optional[int] = ..., equip_type: _Optional[int] = ..., type_attr_lib_id: _Optional[int] = ..., style_effect_lib_id: _Optional[int] = ..., max_durability: _Optional[int] = ..., durability_invalid_type: _Optional[int] = ..., fashion_m_id: _Optional[int] = ..., fashion_f_id: _Optional[int] = ..., bonus_grow_times: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., basic_grow_range: _Optional[int] = ...) -> None: ...

class EquipTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: EquipTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[EquipTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, EquipTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, EquipTableBase]] = ...) -> None: ...
