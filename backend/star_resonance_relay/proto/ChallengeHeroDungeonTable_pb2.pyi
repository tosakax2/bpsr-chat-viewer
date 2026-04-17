import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChallengeHeroDungeonTableBase(_message.Message):
    __slots__ = ("dungeon_id", "dungeon_group", "star_level", "label_pic", "background", "model_id", "effect_id", "extra_target", "base_ratio", "affix", "select_affix", "score_rank", "limit_time", "score_award", "key_reward")
    DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_GROUP_FIELD_NUMBER: _ClassVar[int]
    STAR_LEVEL_FIELD_NUMBER: _ClassVar[int]
    LABEL_PIC_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    EFFECT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_TARGET_FIELD_NUMBER: _ClassVar[int]
    BASE_RATIO_FIELD_NUMBER: _ClassVar[int]
    AFFIX_FIELD_NUMBER: _ClassVar[int]
    SELECT_AFFIX_FIELD_NUMBER: _ClassVar[int]
    SCORE_RANK_FIELD_NUMBER: _ClassVar[int]
    LIMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    SCORE_AWARD_FIELD_NUMBER: _ClassVar[int]
    KEY_REWARD_FIELD_NUMBER: _ClassVar[int]
    dungeon_id: int
    dungeon_group: int
    star_level: int
    label_pic: str
    background: str
    model_id: int
    effect_id: str
    extra_target: _table_basic_pb2.int_array
    base_ratio: int
    affix: _table_basic_pb2.int_table
    select_affix: _table_basic_pb2.int_table
    score_rank: _table_basic_pb2.int_table
    limit_time: int
    score_award: _table_basic_pb2.int_table
    key_reward: _table_basic_pb2.int_array
    def __init__(self, dungeon_id: _Optional[int] = ..., dungeon_group: _Optional[int] = ..., star_level: _Optional[int] = ..., label_pic: _Optional[str] = ..., background: _Optional[str] = ..., model_id: _Optional[int] = ..., effect_id: _Optional[str] = ..., extra_target: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., base_ratio: _Optional[int] = ..., affix: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., select_affix: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., score_rank: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., limit_time: _Optional[int] = ..., score_award: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., key_reward: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class ChallengeHeroDungeonTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ChallengeHeroDungeonTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ChallengeHeroDungeonTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ChallengeHeroDungeonTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ChallengeHeroDungeonTableBase]] = ...) -> None: ...
