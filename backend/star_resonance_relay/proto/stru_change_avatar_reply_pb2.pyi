import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeAvatarReply(_message.Message):
    __slots__ = ("avatar_id", "success", "err_code")
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    avatar_id: int
    success: bool
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, avatar_id: _Optional[int] = ..., success: bool = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
