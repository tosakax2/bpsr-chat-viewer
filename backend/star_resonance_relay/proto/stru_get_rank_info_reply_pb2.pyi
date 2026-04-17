import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_fish_rank_list_pb2 as _stru_fish_rank_list_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetRankInfoReply(_message.Message):
    __slots__ = ("fish_id", "fish_rank_type", "rank_list", "err_code")
    FISH_ID_FIELD_NUMBER: _ClassVar[int]
    FISH_RANK_TYPE_FIELD_NUMBER: _ClassVar[int]
    RANK_LIST_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    fish_id: int
    fish_rank_type: int
    rank_list: _stru_fish_rank_list_pb2.FishRankList
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, fish_id: _Optional[int] = ..., fish_rank_type: _Optional[int] = ..., rank_list: _Optional[_Union[_stru_fish_rank_list_pb2.FishRankList, _Mapping]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
