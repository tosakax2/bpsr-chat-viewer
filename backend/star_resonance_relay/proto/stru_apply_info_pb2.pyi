import stru_user_summary_data_pb2 as _stru_user_summary_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyInfo(_message.Message):
    __slots__ = ("char_id", "time", "user_summary_data")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    USER_SUMMARY_DATA_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    time: int
    user_summary_data: _stru_user_summary_data_pb2.UserSummaryData
    def __init__(self, char_id: _Optional[int] = ..., time: _Optional[int] = ..., user_summary_data: _Optional[_Union[_stru_user_summary_data_pb2.UserSummaryData, _Mapping]] = ...) -> None: ...
