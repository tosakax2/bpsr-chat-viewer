from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FunctionTimeData(_message.Message):
    __slots__ = ("times", "timestamp")
    TIMES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    times: int
    timestamp: int
    def __init__(self, times: _Optional[int] = ..., timestamp: _Optional[int] = ...) -> None: ...
