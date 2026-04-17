import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityAcceptRejectInvitationReply(_message.Message):
    __slots__ = ("err_code", "check_in_content")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    CHECK_IN_CONTENT_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    check_in_content: str
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., check_in_content: _Optional[str] = ...) -> None: ...
