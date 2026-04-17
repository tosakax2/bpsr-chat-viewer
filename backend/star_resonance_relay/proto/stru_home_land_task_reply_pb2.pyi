import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_home_land_player_task_info_pb2 as _stru_home_land_player_task_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeLandTaskReply(_message.Message):
    __slots__ = ("err_code", "task_info")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    task_info: _stru_home_land_player_task_info_pb2.HomeLandPlayerTaskInfo
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., task_info: _Optional[_Union[_stru_home_land_player_task_info_pb2.HomeLandPlayerTaskInfo, _Mapping]] = ...) -> None: ...
