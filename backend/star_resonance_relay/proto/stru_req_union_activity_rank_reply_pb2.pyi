import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_union_activity_rank_info_pb2 as _stru_union_activity_rank_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReqUnionActivityRankReply(_message.Message):
    __slots__ = ("rank_list", "err_code")
    RANK_LIST_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    rank_list: _containers.RepeatedCompositeFieldContainer[_stru_union_activity_rank_info_pb2.UnionActivityRankInfo]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, rank_list: _Optional[_Iterable[_Union[_stru_union_activity_rank_info_pb2.UnionActivityRankInfo, _Mapping]]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
