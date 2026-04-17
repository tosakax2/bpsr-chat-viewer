import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TipsInfo(_message.Message):
    __slots__ = ("tips_type", "err_code", "tips_params")
    TIPS_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    TIPS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    tips_type: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    tips_params: bytes
    def __init__(self, tips_type: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., tips_params: _Optional[bytes] = ...) -> None: ...
