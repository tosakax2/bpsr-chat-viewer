from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NoticeInfo(_message.Message):
    __slots__ = ("notice_id", "send_time", "is_loop", "loop_number", "loop_time_interval", "content_text", "end_time")
    NOTICE_ID_FIELD_NUMBER: _ClassVar[int]
    SEND_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_LOOP_FIELD_NUMBER: _ClassVar[int]
    LOOP_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LOOP_TIME_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TEXT_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    notice_id: int
    send_time: int
    is_loop: bool
    loop_number: int
    loop_time_interval: int
    content_text: str
    end_time: int
    def __init__(self, notice_id: _Optional[int] = ..., send_time: _Optional[int] = ..., is_loop: bool = ..., loop_number: _Optional[int] = ..., loop_time_interval: _Optional[int] = ..., content_text: _Optional[str] = ..., end_time: _Optional[int] = ...) -> None: ...
