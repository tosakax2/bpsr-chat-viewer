import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FishingResultReportReply(_message.Message):
    __slots__ = ("durability_exhausted", "is_burst", "bait_exhausted", "size", "size_new_record", "err_code")
    DURABILITY_EXHAUSTED_FIELD_NUMBER: _ClassVar[int]
    IS_BURST_FIELD_NUMBER: _ClassVar[int]
    BAIT_EXHAUSTED_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SIZE_NEW_RECORD_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    durability_exhausted: bool
    is_burst: bool
    bait_exhausted: bool
    size: int
    size_new_record: bool
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, durability_exhausted: bool = ..., is_burst: bool = ..., bait_exhausted: bool = ..., size: _Optional[int] = ..., size_new_record: bool = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
