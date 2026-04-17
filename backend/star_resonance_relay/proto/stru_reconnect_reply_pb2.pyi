import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReconnectReply(_message.Message):
    __slots__ = ("account_id", "char_id", "is_privilege", "is_change_account", "err_code")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVILEGE_FIELD_NUMBER: _ClassVar[int]
    IS_CHANGE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    char_id: int
    is_privilege: bool
    is_change_account: bool
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, account_id: _Optional[str] = ..., char_id: _Optional[int] = ..., is_privilege: bool = ..., is_change_account: bool = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
