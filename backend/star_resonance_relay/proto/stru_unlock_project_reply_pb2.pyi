import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_profession_project_common_sync_data_pb2 as _stru_profession_project_common_sync_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnlockProjectReply(_message.Message):
    __slots__ = ("sync_data", "current_project_id", "err_code")
    SYNC_DATA_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    sync_data: _stru_profession_project_common_sync_data_pb2.ProfessionProjectCommonSyncData
    current_project_id: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, sync_data: _Optional[_Union[_stru_profession_project_common_sync_data_pb2.ProfessionProjectCommonSyncData, _Mapping]] = ..., current_project_id: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
