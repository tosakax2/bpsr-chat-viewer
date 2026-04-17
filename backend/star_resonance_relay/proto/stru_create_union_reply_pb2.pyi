import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_union_info_pb2 as _stru_union_info_pb2
import stru_user_summary_data_pb2 as _stru_user_summary_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateUnionReply(_message.Message):
    __slots__ = ("next_join_time", "info", "president_info", "err_code")
    NEXT_JOIN_TIME_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    PRESIDENT_INFO_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    next_join_time: int
    info: _stru_union_info_pb2.UnionInfo
    president_info: _stru_user_summary_data_pb2.UserSummaryData
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, next_join_time: _Optional[int] = ..., info: _Optional[_Union[_stru_union_info_pb2.UnionInfo, _Mapping]] = ..., president_info: _Optional[_Union[_stru_user_summary_data_pb2.UserSummaryData, _Mapping]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
