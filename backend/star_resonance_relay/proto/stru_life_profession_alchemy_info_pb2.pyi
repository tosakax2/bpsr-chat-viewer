from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LifeProfessionAlchemyInfo(_message.Message):
    __slots__ = ("failure_count", "rd_count", "last_reset_time")
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    RD_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_RESET_TIME_FIELD_NUMBER: _ClassVar[int]
    failure_count: int
    rd_count: int
    last_reset_time: int
    def __init__(self, failure_count: _Optional[int] = ..., rd_count: _Optional[int] = ..., last_reset_time: _Optional[int] = ...) -> None: ...
