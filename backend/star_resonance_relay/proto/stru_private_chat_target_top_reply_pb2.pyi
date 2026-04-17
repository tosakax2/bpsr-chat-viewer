import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrivateChatTargetTopReply(_message.Message):
    __slots__ = ("target_id", "set_top", "err_code")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    SET_TOP_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    target_id: int
    set_top: bool
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, target_id: _Optional[int] = ..., set_top: bool = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
