import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonGlobalTableBase(_message.Message):
    __slots__ = ("season_id", "season_name", "season_time_id", "min_equip_level", "max_equip_level", "max_weapon_level", "battle_pass_card_id")
    SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    SEASON_NAME_FIELD_NUMBER: _ClassVar[int]
    SEASON_TIME_ID_FIELD_NUMBER: _ClassVar[int]
    MIN_EQUIP_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAX_EQUIP_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAX_WEAPON_LEVEL_FIELD_NUMBER: _ClassVar[int]
    BATTLE_PASS_CARD_ID_FIELD_NUMBER: _ClassVar[int]
    season_id: int
    season_name: _table_basic_pb2.mlstring
    season_time_id: int
    min_equip_level: int
    max_equip_level: int
    max_weapon_level: int
    battle_pass_card_id: int
    def __init__(self, season_id: _Optional[int] = ..., season_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., season_time_id: _Optional[int] = ..., min_equip_level: _Optional[int] = ..., max_equip_level: _Optional[int] = ..., max_weapon_level: _Optional[int] = ..., battle_pass_card_id: _Optional[int] = ...) -> None: ...

class SeasonGlobalTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SeasonGlobalTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SeasonGlobalTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SeasonGlobalTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SeasonGlobalTableBase]] = ...) -> None: ...
