import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_session_info_pb2 as _stru_session_info_pb2
import stru_text_check_data_result_pb2 as _stru_text_check_data_result_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TextCheckReply(_message.Message):
    __slots__ = ("session", "check_data_result", "err_code")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    CHECK_DATA_RESULT_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    session: _stru_session_info_pb2.SessionInfo
    check_data_result: _stru_text_check_data_result_pb2.TextCheckDataResult
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, session: _Optional[_Union[_stru_session_info_pb2.SessionInfo, _Mapping]] = ..., check_data_result: _Optional[_Union[_stru_text_check_data_result_pb2.TextCheckDataResult, _Mapping]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
