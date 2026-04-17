import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_tmp_token_result_pb2 as _stru_tmp_token_result_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RetAvatarTokenRequest(_message.Message):
    __slots__ = ("err_code", "result")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    result: _stru_tmp_token_result_pb2.TmpTokenResult
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., result: _Optional[_Union[_stru_tmp_token_result_pb2.TmpTokenResult, _Mapping]] = ...) -> None: ...
