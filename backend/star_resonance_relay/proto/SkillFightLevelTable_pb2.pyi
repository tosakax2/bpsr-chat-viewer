import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkillFightLevelTableBase(_message.Message):
    __slots__ = ("id", "skill_id", "level", "skill_effect_id", "name", "skill_cost", "skill_res_check", "pve_cool_time", "float_parameter", "show_parameter")
    ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SKILL_EFFECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SKILL_COST_FIELD_NUMBER: _ClassVar[int]
    SKILL_RES_CHECK_FIELD_NUMBER: _ClassVar[int]
    PVE_COOL_TIME_FIELD_NUMBER: _ClassVar[int]
    FLOAT_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    SHOW_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    id: int
    skill_id: int
    level: int
    skill_effect_id: int
    name: str
    skill_cost: _table_basic_pb2.int_table
    skill_res_check: _table_basic_pb2.int_table
    pve_cool_time: float
    float_parameter: _table_basic_pb2.string_table
    show_parameter: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., skill_id: _Optional[int] = ..., level: _Optional[int] = ..., skill_effect_id: _Optional[int] = ..., name: _Optional[str] = ..., skill_cost: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., skill_res_check: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., pve_cool_time: _Optional[float] = ..., float_parameter: _Optional[_Union[_table_basic_pb2.string_table, _Mapping]] = ..., show_parameter: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class SkillFightLevelTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SkillFightLevelTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SkillFightLevelTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SkillFightLevelTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SkillFightLevelTableBase]] = ...) -> None: ...
