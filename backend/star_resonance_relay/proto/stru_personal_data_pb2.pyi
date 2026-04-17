import stru_personal_info_pb2 as _stru_personal_info_pb2
import stru_user_summary_data_pb2 as _stru_user_summary_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PersonalData(_message.Message):
    __slots__ = ("char_id", "info", "social_data")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_DATA_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    info: _stru_personal_info_pb2.PersonalInfo
    social_data: _stru_user_summary_data_pb2.UserSummaryData
    def __init__(self, char_id: _Optional[int] = ..., info: _Optional[_Union[_stru_personal_info_pb2.PersonalInfo, _Mapping]] = ..., social_data: _Optional[_Union[_stru_user_summary_data_pb2.UserSummaryData, _Mapping]] = ...) -> None: ...
