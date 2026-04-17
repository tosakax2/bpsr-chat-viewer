import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GmResult(_message.Message):
    __slots__ = ("success", "fail_reason", "ret_params", "err_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAIL_REASON_FIELD_NUMBER: _ClassVar[int]
    RET_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    fail_reason: str
    ret_params: _containers.RepeatedScalarFieldContainer[str]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, success: bool = ..., fail_reason: _Optional[str] = ..., ret_params: _Optional[_Iterable[str]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
