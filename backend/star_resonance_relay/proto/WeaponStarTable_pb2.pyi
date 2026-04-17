import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WeaponStarTableBase(_message.Message):
    __slots__ = ("id", "weapon_id", "skill_id", "ulock_skill_level", "change_skill", "upgrade_cost", "upgrade_extra_cost", "buff_id", "buff_par", "upgrade_skill_id", "upgrade_skill_level", "name", "des")
    ID_FIELD_NUMBER: _ClassVar[int]
    WEAPON_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    ULOCK_SKILL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CHANGE_SKILL_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_COST_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_EXTRA_COST_FIELD_NUMBER: _ClassVar[int]
    BUFF_ID_FIELD_NUMBER: _ClassVar[int]
    BUFF_PAR_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_SKILL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DES_FIELD_NUMBER: _ClassVar[int]
    id: int
    weapon_id: int
    skill_id: int
    ulock_skill_level: _table_basic_pb2.int_table
    change_skill: int
    upgrade_cost: _table_basic_pb2.int_table
    upgrade_extra_cost: _table_basic_pb2.int_table
    buff_id: int
    buff_par: _table_basic_pb2.int_array
    upgrade_skill_id: _table_basic_pb2.int_array
    upgrade_skill_level: _table_basic_pb2.int_array
    name: _table_basic_pb2.mlstring
    des: _table_basic_pb2.mlstring
    def __init__(self, id: _Optional[int] = ..., weapon_id: _Optional[int] = ..., skill_id: _Optional[int] = ..., ulock_skill_level: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., change_skill: _Optional[int] = ..., upgrade_cost: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., upgrade_extra_cost: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., buff_id: _Optional[int] = ..., buff_par: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., upgrade_skill_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., upgrade_skill_level: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ...) -> None: ...

class WeaponStarTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: WeaponStarTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[WeaponStarTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, WeaponStarTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, WeaponStarTableBase]] = ...) -> None: ...
