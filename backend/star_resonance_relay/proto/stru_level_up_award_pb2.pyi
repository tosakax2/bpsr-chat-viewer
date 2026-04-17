from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LevelUpAward(_message.Message):
    __slots__ = ("drop_times", "last_drop_time")
    DROP_TIMES_FIELD_NUMBER: _ClassVar[int]
    LAST_DROP_TIME_FIELD_NUMBER: _ClassVar[int]
    drop_times: int
    last_drop_time: int
    def __init__(self, drop_times: _Optional[int] = ..., last_drop_time: _Optional[int] = ...) -> None: ...
