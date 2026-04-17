import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityBuildLifeProfessionReply(_message.Message):
    __slots__ = ("err_code", "build_uuid")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    BUILD_UUID_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    build_uuid: int
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., build_uuid: _Optional[int] = ...) -> None: ...
