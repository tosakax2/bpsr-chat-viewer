import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_fish_rank_info_pb2 as _stru_fish_rank_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFishRankTopReply(_message.Message):
    __slots__ = ("fish_area_id", "rank_list", "err_code")
    class RankListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_fish_rank_info_pb2.FishRankInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_fish_rank_info_pb2.FishRankInfo, _Mapping]] = ...) -> None: ...
    FISH_AREA_ID_FIELD_NUMBER: _ClassVar[int]
    RANK_LIST_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    fish_area_id: int
    rank_list: _containers.MessageMap[int, _stru_fish_rank_info_pb2.FishRankInfo]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, fish_area_id: _Optional[int] = ..., rank_list: _Optional[_Mapping[int, _stru_fish_rank_info_pb2.FishRankInfo]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
