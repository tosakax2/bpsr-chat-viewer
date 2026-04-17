import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntityAttributeTableBase(_message.Message):
    __slots__ = ("id", "comment", "season", "equip_level", "equip_level_variate", "max_hp", "attack", "defense", "ignore_defense", "ignore_defense_pct", "fire_defense", "water_defense", "wood_defense", "electricity_defense", "wind_defense", "rock_defense", "light_defense", "dark_defense", "max_stunned", "max_extinction", "crit_resist", "meter_value")
    ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    SEASON_FIELD_NUMBER: _ClassVar[int]
    EQUIP_LEVEL_FIELD_NUMBER: _ClassVar[int]
    EQUIP_LEVEL_VARIATE_FIELD_NUMBER: _ClassVar[int]
    MAX_HP_FIELD_NUMBER: _ClassVar[int]
    ATTACK_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_DEFENSE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_DEFENSE_PCT_FIELD_NUMBER: _ClassVar[int]
    FIRE_DEFENSE_FIELD_NUMBER: _ClassVar[int]
    WATER_DEFENSE_FIELD_NUMBER: _ClassVar[int]
    WOOD_DEFENSE_FIELD_NUMBER: _ClassVar[int]
    ELECTRICITY_DEFENSE_FIELD_NUMBER: _ClassVar[int]
    WIND_DEFENSE_FIELD_NUMBER: _ClassVar[int]
    ROCK_DEFENSE_FIELD_NUMBER: _ClassVar[int]
    LIGHT_DEFENSE_FIELD_NUMBER: _ClassVar[int]
    DARK_DEFENSE_FIELD_NUMBER: _ClassVar[int]
    MAX_STUNNED_FIELD_NUMBER: _ClassVar[int]
    MAX_EXTINCTION_FIELD_NUMBER: _ClassVar[int]
    CRIT_RESIST_FIELD_NUMBER: _ClassVar[int]
    METER_VALUE_FIELD_NUMBER: _ClassVar[int]
    id: int
    comment: str
    season: int
    equip_level: int
    equip_level_variate: int
    max_hp: int
    attack: int
    defense: int
    ignore_defense: int
    ignore_defense_pct: int
    fire_defense: int
    water_defense: int
    wood_defense: int
    electricity_defense: int
    wind_defense: int
    rock_defense: int
    light_defense: int
    dark_defense: int
    max_stunned: int
    max_extinction: int
    crit_resist: int
    meter_value: _table_basic_pb2.int_table
    def __init__(self, id: _Optional[int] = ..., comment: _Optional[str] = ..., season: _Optional[int] = ..., equip_level: _Optional[int] = ..., equip_level_variate: _Optional[int] = ..., max_hp: _Optional[int] = ..., attack: _Optional[int] = ..., defense: _Optional[int] = ..., ignore_defense: _Optional[int] = ..., ignore_defense_pct: _Optional[int] = ..., fire_defense: _Optional[int] = ..., water_defense: _Optional[int] = ..., wood_defense: _Optional[int] = ..., electricity_defense: _Optional[int] = ..., wind_defense: _Optional[int] = ..., rock_defense: _Optional[int] = ..., light_defense: _Optional[int] = ..., dark_defense: _Optional[int] = ..., max_stunned: _Optional[int] = ..., max_extinction: _Optional[int] = ..., crit_resist: _Optional[int] = ..., meter_value: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class EntityAttributeTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: EntityAttributeTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[EntityAttributeTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, EntityAttributeTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, EntityAttributeTableBase]] = ...) -> None: ...
