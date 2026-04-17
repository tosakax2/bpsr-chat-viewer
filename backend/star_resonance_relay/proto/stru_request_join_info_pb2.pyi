import stru_apply_join_info_pb2 as _stru_apply_join_info_pb2
import stru_user_summary_data_pb2 as _stru_user_summary_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestJoinInfo(_message.Message):
    __slots__ = ("social_data", "apply_info")
    SOCIAL_DATA_FIELD_NUMBER: _ClassVar[int]
    APPLY_INFO_FIELD_NUMBER: _ClassVar[int]
    social_data: _stru_user_summary_data_pb2.UserSummaryData
    apply_info: _stru_apply_join_info_pb2.ApplyJoinInfo
    def __init__(self, social_data: _Optional[_Union[_stru_user_summary_data_pb2.UserSummaryData, _Mapping]] = ..., apply_info: _Optional[_Union[_stru_apply_join_info_pb2.ApplyJoinInfo, _Mapping]] = ...) -> None: ...
