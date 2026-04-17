import stru_dungeon_award_pb2 as _stru_dungeon_award_pb2
import stru_dungeon_boss_rank_pb2 as _stru_dungeon_boss_rank_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonWorldBossSettlement(_message.Message):
    __slots__ = ("boss_hp_percent", "dungeon_boss_rank", "award", "boss_rank_award", "last_hit_award")
    class AwardEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_dungeon_award_pb2.DungeonAward
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_dungeon_award_pb2.DungeonAward, _Mapping]] = ...) -> None: ...
    class BossRankAwardEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_dungeon_award_pb2.DungeonAward
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_dungeon_award_pb2.DungeonAward, _Mapping]] = ...) -> None: ...
    class LastHitAwardEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_dungeon_award_pb2.DungeonAward
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_dungeon_award_pb2.DungeonAward, _Mapping]] = ...) -> None: ...
    BOSS_HP_PERCENT_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_BOSS_RANK_FIELD_NUMBER: _ClassVar[int]
    AWARD_FIELD_NUMBER: _ClassVar[int]
    BOSS_RANK_AWARD_FIELD_NUMBER: _ClassVar[int]
    LAST_HIT_AWARD_FIELD_NUMBER: _ClassVar[int]
    boss_hp_percent: int
    dungeon_boss_rank: _stru_dungeon_boss_rank_pb2.DungeonBossRank
    award: _containers.MessageMap[int, _stru_dungeon_award_pb2.DungeonAward]
    boss_rank_award: _containers.MessageMap[int, _stru_dungeon_award_pb2.DungeonAward]
    last_hit_award: _containers.MessageMap[int, _stru_dungeon_award_pb2.DungeonAward]
    def __init__(self, boss_hp_percent: _Optional[int] = ..., dungeon_boss_rank: _Optional[_Union[_stru_dungeon_boss_rank_pb2.DungeonBossRank, _Mapping]] = ..., award: _Optional[_Mapping[int, _stru_dungeon_award_pb2.DungeonAward]] = ..., boss_rank_award: _Optional[_Mapping[int, _stru_dungeon_award_pb2.DungeonAward]] = ..., last_hit_award: _Optional[_Mapping[int, _stru_dungeon_award_pb2.DungeonAward]] = ...) -> None: ...
