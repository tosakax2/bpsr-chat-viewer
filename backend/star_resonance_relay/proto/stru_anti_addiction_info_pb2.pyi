from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AntiAddictionInfo(_message.Message):
    __slots__ = ("last_time",)
    LAST_TIME_FIELD_NUMBER: _ClassVar[int]
    last_time: int
    def __init__(self, last_time: _Optional[int] = ...) -> None: ...
