import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrivilegeActivateReply(_message.Message):
    __slots__ = ("err_code", "is_privilege", "is_change_account")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVILEGE_FIELD_NUMBER: _ClassVar[int]
    IS_CHANGE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    is_privilege: bool
    is_change_account: bool
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., is_privilege: bool = ..., is_change_account: bool = ...) -> None: ...
