import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_union_member_pb2 as _stru_union_member_pb2
import stru_user_summary_data_pb2 as _stru_user_summary_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReqUnionMemsListReply(_message.Message):
    __slots__ = ("mem_list", "mem_social_list", "err_code")
    MEM_LIST_FIELD_NUMBER: _ClassVar[int]
    MEM_SOCIAL_LIST_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    mem_list: _containers.RepeatedCompositeFieldContainer[_stru_union_member_pb2.UnionMember]
    mem_social_list: _containers.RepeatedCompositeFieldContainer[_stru_user_summary_data_pb2.UserSummaryData]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, mem_list: _Optional[_Iterable[_Union[_stru_union_member_pb2.UnionMember, _Mapping]]] = ..., mem_social_list: _Optional[_Iterable[_Union[_stru_user_summary_data_pb2.UserSummaryData, _Mapping]]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
