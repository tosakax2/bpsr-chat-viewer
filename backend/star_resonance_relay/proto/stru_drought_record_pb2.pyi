from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DroughtRecord(_message.Message):
    __slots__ = ("trigger_time", "segment_id", "duration", "actual_end_time", "is_watered", "is_expired")
    TRIGGER_TIME_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_END_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_WATERED_FIELD_NUMBER: _ClassVar[int]
    IS_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    trigger_time: int
    segment_id: int
    duration: int
    actual_end_time: int
    is_watered: bool
    is_expired: bool
    def __init__(self, trigger_time: _Optional[int] = ..., segment_id: _Optional[int] = ..., duration: _Optional[int] = ..., actual_end_time: _Optional[int] = ..., is_watered: bool = ..., is_expired: bool = ...) -> None: ...
