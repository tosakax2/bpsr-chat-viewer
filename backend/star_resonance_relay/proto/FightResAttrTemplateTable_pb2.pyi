import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FightResAttrTemplateTableBase(_message.Message):
    __slots__ = ("id", "res_i_ds", "desc", "int_params", "int_params1", "int_params2", "ui_name", "bind_elemental", "bind_skill_id", "inner_ring_factor", "battle_res_icon", "inner_color")
    ID_FIELD_NUMBER: _ClassVar[int]
    RES_I_DS_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    INT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INT_PARAMS1_FIELD_NUMBER: _ClassVar[int]
    INT_PARAMS2_FIELD_NUMBER: _ClassVar[int]
    UI_NAME_FIELD_NUMBER: _ClassVar[int]
    BIND_ELEMENTAL_FIELD_NUMBER: _ClassVar[int]
    BIND_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    INNER_RING_FACTOR_FIELD_NUMBER: _ClassVar[int]
    BATTLE_RES_ICON_FIELD_NUMBER: _ClassVar[int]
    INNER_COLOR_FIELD_NUMBER: _ClassVar[int]
    id: int
    res_i_ds: _table_basic_pb2.int_array
    desc: str
    int_params: _table_basic_pb2.int_array
    int_params1: _table_basic_pb2.int_table
    int_params2: _table_basic_pb2.int_table
    ui_name: str
    bind_elemental: int
    bind_skill_id: _table_basic_pb2.int_array
    inner_ring_factor: float
    battle_res_icon: str
    inner_color: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., res_i_ds: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., desc: _Optional[str] = ..., int_params: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., int_params1: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., int_params2: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., ui_name: _Optional[str] = ..., bind_elemental: _Optional[int] = ..., bind_skill_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., inner_ring_factor: _Optional[float] = ..., battle_res_icon: _Optional[str] = ..., inner_color: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class FightResAttrTemplateTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FightResAttrTemplateTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FightResAttrTemplateTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FightResAttrTemplateTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FightResAttrTemplateTableBase]] = ...) -> None: ...
