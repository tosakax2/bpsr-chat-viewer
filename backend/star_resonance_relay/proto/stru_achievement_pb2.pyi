from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Achievement(_message.Message):
    __slots__ = ("finish_num", "has_received", "begin_progress")
    FINISH_NUM_FIELD_NUMBER: _ClassVar[int]
    HAS_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    BEGIN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    finish_num: int
    has_received: bool
    begin_progress: int
    def __init__(self, finish_num: _Optional[int] = ..., has_received: bool = ..., begin_progress: _Optional[int] = ...) -> None: ...
