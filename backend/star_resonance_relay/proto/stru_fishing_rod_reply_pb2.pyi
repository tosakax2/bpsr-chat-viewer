import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FishingRodReply(_message.Message):
    __slots__ = ("fish_id", "wait_mills", "err_code")
    FISH_ID_FIELD_NUMBER: _ClassVar[int]
    WAIT_MILLS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    fish_id: int
    wait_mills: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, fish_id: _Optional[int] = ..., wait_mills: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
