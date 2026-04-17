import stru_user_summary_data_pb2 as _stru_user_summary_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GrowFundMemInfo(_message.Message):
    __slots__ = ("fund_pos", "basic_avatar_data")
    FUND_POS_FIELD_NUMBER: _ClassVar[int]
    BASIC_AVATAR_DATA_FIELD_NUMBER: _ClassVar[int]
    fund_pos: int
    basic_avatar_data: _stru_user_summary_data_pb2.UserSummaryData
    def __init__(self, fund_pos: _Optional[int] = ..., basic_avatar_data: _Optional[_Union[_stru_user_summary_data_pb2.UserSummaryData, _Mapping]] = ...) -> None: ...
