import stru_season_rank_info_pb2 as _stru_season_rank_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonRankList(_message.Message):
    __slots__ = ("season_rank_list", "show_armband_id")
    class SeasonRankListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_season_rank_info_pb2.SeasonRankInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_season_rank_info_pb2.SeasonRankInfo, _Mapping]] = ...) -> None: ...
    SEASON_RANK_LIST_FIELD_NUMBER: _ClassVar[int]
    SHOW_ARMBAND_ID_FIELD_NUMBER: _ClassVar[int]
    season_rank_list: _containers.MessageMap[int, _stru_season_rank_info_pb2.SeasonRankInfo]
    show_armband_id: int
    def __init__(self, season_rank_list: _Optional[_Mapping[int, _stru_season_rank_info_pb2.SeasonRankInfo]] = ..., show_armband_id: _Optional[int] = ...) -> None: ...
