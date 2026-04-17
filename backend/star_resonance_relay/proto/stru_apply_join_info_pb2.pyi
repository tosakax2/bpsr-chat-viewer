from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyJoinInfo(_message.Message):
    __slots__ = ("char_id", "request_time")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIME_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    request_time: int
    def __init__(self, char_id: _Optional[int] = ..., request_time: _Optional[int] = ...) -> None: ...
