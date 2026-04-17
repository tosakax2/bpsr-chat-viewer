from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TimerRefreshInfo(_message.Message):
    __slots__ = ("last_refresh_time",)
    LAST_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    last_refresh_time: int
    def __init__(self, last_refresh_time: _Optional[int] = ...) -> None: ...
