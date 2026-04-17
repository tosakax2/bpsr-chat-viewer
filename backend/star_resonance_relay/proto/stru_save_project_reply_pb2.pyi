import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_profession_project_common_sync_data_pb2 as _stru_profession_project_common_sync_data_pb2
import stru_project_extra_sync_data_pb2 as _stru_project_extra_sync_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SaveProjectReply(_message.Message):
    __slots__ = ("sync_data", "saved_project_id", "current_project_sync_data", "err_code")
    SYNC_DATA_FIELD_NUMBER: _ClassVar[int]
    SAVED_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PROJECT_SYNC_DATA_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    sync_data: _stru_profession_project_common_sync_data_pb2.ProfessionProjectCommonSyncData
    saved_project_id: int
    current_project_sync_data: _stru_project_extra_sync_data_pb2.ProjectExtraSyncData
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, sync_data: _Optional[_Union[_stru_profession_project_common_sync_data_pb2.ProfessionProjectCommonSyncData, _Mapping]] = ..., saved_project_id: _Optional[int] = ..., current_project_sync_data: _Optional[_Union[_stru_project_extra_sync_data_pb2.ProjectExtraSyncData, _Mapping]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
