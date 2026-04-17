import stru_world_boss_rank_info_pb2 as _stru_world_boss_rank_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorldBossRankInfoParam(_message.Message):
    __slots__ = ("rank_infos",)
    RANK_INFOS_FIELD_NUMBER: _ClassVar[int]
    rank_infos: _containers.RepeatedCompositeFieldContainer[_stru_world_boss_rank_info_pb2.WorldBossRankInfo]
    def __init__(self, rank_infos: _Optional[_Iterable[_Union[_stru_world_boss_rank_info_pb2.WorldBossRankInfo, _Mapping]]] = ...) -> None: ...
