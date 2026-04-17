import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunitySetNameReply(_message.Message):
    __slots__ = ("err_code", "time")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    time: int
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., time: _Optional[int] = ...) -> None: ...
