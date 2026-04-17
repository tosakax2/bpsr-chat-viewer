import stru_rank_data_pb2 as _stru_rank_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonBossRank(_message.Message):
    __slots__ = ("boss_rank",)
    class BossRankEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_rank_data_pb2.RankData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_rank_data_pb2.RankData, _Mapping]] = ...) -> None: ...
    BOSS_RANK_FIELD_NUMBER: _ClassVar[int]
    boss_rank: _containers.MessageMap[int, _stru_rank_data_pb2.RankData]
    def __init__(self, boss_rank: _Optional[_Mapping[int, _stru_rank_data_pb2.RankData]] = ...) -> None: ...
