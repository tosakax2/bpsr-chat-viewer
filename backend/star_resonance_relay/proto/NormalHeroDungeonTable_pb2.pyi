import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NormalHeroDungeonTableBase(_message.Message):
    __slots__ = ("dungeon_id", "season_open_time", "affix_pool", "background", "model_id", "effect_id", "base_ratio", "limit_time", "score_rank", "key_reward")
    DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    SEASON_OPEN_TIME_FIELD_NUMBER: _ClassVar[int]
    AFFIX_POOL_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    EFFECT_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_RATIO_FIELD_NUMBER: _ClassVar[int]
    LIMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    SCORE_RANK_FIELD_NUMBER: _ClassVar[int]
    KEY_REWARD_FIELD_NUMBER: _ClassVar[int]
    dungeon_id: int
    season_open_time: int
    affix_pool: int
    background: str
    model_id: int
    effect_id: int
    base_ratio: int
    limit_time: int
    score_rank: _table_basic_pb2.int_table
    key_reward: _table_basic_pb2.int_array
    def __init__(self, dungeon_id: _Optional[int] = ..., season_open_time: _Optional[int] = ..., affix_pool: _Optional[int] = ..., background: _Optional[str] = ..., model_id: _Optional[int] = ..., effect_id: _Optional[int] = ..., base_ratio: _Optional[int] = ..., limit_time: _Optional[int] = ..., score_rank: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., key_reward: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class NormalHeroDungeonTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: NormalHeroDungeonTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[NormalHeroDungeonTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, NormalHeroDungeonTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, NormalHeroDungeonTableBase]] = ...) -> None: ...
