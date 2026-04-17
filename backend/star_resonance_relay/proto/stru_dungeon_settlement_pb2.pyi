import stru_dungeon_award_pb2 as _stru_dungeon_award_pb2
import stru_dungeon_world_boss_settlement_pb2 as _stru_dungeon_world_boss_settlement_pb2
import stru_settlement_position_pb2 as _stru_settlement_position_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonSettlement(_message.Message):
    __slots__ = ("pass_time", "award", "settlement_pos", "world_boss_settlement", "master_mode_score")
    class AwardEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_dungeon_award_pb2.DungeonAward
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_dungeon_award_pb2.DungeonAward, _Mapping]] = ...) -> None: ...
    class SettlementPosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_settlement_position_pb2.SettlementPosition
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_settlement_position_pb2.SettlementPosition, _Mapping]] = ...) -> None: ...
    PASS_TIME_FIELD_NUMBER: _ClassVar[int]
    AWARD_FIELD_NUMBER: _ClassVar[int]
    SETTLEMENT_POS_FIELD_NUMBER: _ClassVar[int]
    WORLD_BOSS_SETTLEMENT_FIELD_NUMBER: _ClassVar[int]
    MASTER_MODE_SCORE_FIELD_NUMBER: _ClassVar[int]
    pass_time: int
    award: _containers.MessageMap[int, _stru_dungeon_award_pb2.DungeonAward]
    settlement_pos: _containers.MessageMap[int, _stru_settlement_position_pb2.SettlementPosition]
    world_boss_settlement: _stru_dungeon_world_boss_settlement_pb2.DungeonWorldBossSettlement
    master_mode_score: int
    def __init__(self, pass_time: _Optional[int] = ..., award: _Optional[_Mapping[int, _stru_dungeon_award_pb2.DungeonAward]] = ..., settlement_pos: _Optional[_Mapping[int, _stru_settlement_position_pb2.SettlementPosition]] = ..., world_boss_settlement: _Optional[_Union[_stru_dungeon_world_boss_settlement_pb2.DungeonWorldBossSettlement, _Mapping]] = ..., master_mode_score: _Optional[int] = ...) -> None: ...
