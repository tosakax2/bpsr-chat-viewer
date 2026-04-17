import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BattlePassCardTableBase(_message.Message):
    __slots__ = ("id", "battle_pass_card_id", "season_level", "season_exp", "free_award", "paid_award", "key_award")
    ID_FIELD_NUMBER: _ClassVar[int]
    BATTLE_PASS_CARD_ID_FIELD_NUMBER: _ClassVar[int]
    SEASON_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SEASON_EXP_FIELD_NUMBER: _ClassVar[int]
    FREE_AWARD_FIELD_NUMBER: _ClassVar[int]
    PAID_AWARD_FIELD_NUMBER: _ClassVar[int]
    KEY_AWARD_FIELD_NUMBER: _ClassVar[int]
    id: int
    battle_pass_card_id: int
    season_level: int
    season_exp: int
    free_award: _table_basic_pb2.int_array
    paid_award: _table_basic_pb2.int_array
    key_award: int
    def __init__(self, id: _Optional[int] = ..., battle_pass_card_id: _Optional[int] = ..., season_level: _Optional[int] = ..., season_exp: _Optional[int] = ..., free_award: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., paid_award: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., key_award: _Optional[int] = ...) -> None: ...

class BattlePassCardTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BattlePassCardTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BattlePassCardTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, BattlePassCardTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, BattlePassCardTableBase]] = ...) -> None: ...
