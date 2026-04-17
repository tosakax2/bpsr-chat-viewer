import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryChatMuteReply(_message.Message):
    __slots__ = ("is_ban", "end_timestamp", "ban_reason", "err_code")
    IS_BAN_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    BAN_REASON_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    is_ban: bool
    end_timestamp: int
    ban_reason: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, is_ban: bool = ..., end_timestamp: _Optional[int] = ..., ban_reason: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
