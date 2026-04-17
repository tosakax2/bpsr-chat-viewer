import stru_fish_rank_info_pb2 as _stru_fish_rank_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FishRankList(_message.Message):
    __slots__ = ("self_info", "rank_list")
    SELF_INFO_FIELD_NUMBER: _ClassVar[int]
    RANK_LIST_FIELD_NUMBER: _ClassVar[int]
    self_info: _stru_fish_rank_info_pb2.FishRankInfo
    rank_list: _containers.RepeatedCompositeFieldContainer[_stru_fish_rank_info_pb2.FishRankInfo]
    def __init__(self, self_info: _Optional[_Union[_stru_fish_rank_info_pb2.FishRankInfo, _Mapping]] = ..., rank_list: _Optional[_Iterable[_Union[_stru_fish_rank_info_pb2.FishRankInfo, _Mapping]]] = ...) -> None: ...
