from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FightResCD(_message.Message):
    __slots__ = ("ResId", "BeginTime", "Duration", "ValidCDTime")
    RESID_FIELD_NUMBER: _ClassVar[int]
    BEGINTIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    VALIDCDTIME_FIELD_NUMBER: _ClassVar[int]
    ResId: int
    BeginTime: int
    Duration: int
    ValidCDTime: int
    def __init__(self, ResId: _Optional[int] = ..., BeginTime: _Optional[int] = ..., Duration: _Optional[int] = ..., ValidCDTime: _Optional[int] = ...) -> None: ...
