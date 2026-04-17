import stru_user_summary_data_pb2 as _stru_user_summary_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SocialInfo(_message.Message):
    __slots__ = ("remark", "remind", "top", "group_id", "social_data", "last_refresh_time")
    REMARK_FIELD_NUMBER: _ClassVar[int]
    REMIND_FIELD_NUMBER: _ClassVar[int]
    TOP_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_DATA_FIELD_NUMBER: _ClassVar[int]
    LAST_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    remark: str
    remind: bool
    top: bool
    group_id: int
    social_data: _stru_user_summary_data_pb2.UserSummaryData
    last_refresh_time: int
    def __init__(self, remark: _Optional[str] = ..., remind: bool = ..., top: bool = ..., group_id: _Optional[int] = ..., social_data: _Optional[_Union[_stru_user_summary_data_pb2.UserSummaryData, _Mapping]] = ..., last_refresh_time: _Optional[int] = ...) -> None: ...
