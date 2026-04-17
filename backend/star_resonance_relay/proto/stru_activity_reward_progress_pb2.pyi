from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ActivityRewardProgress(_message.Message):
    __slots__ = ("cur", "max")
    CUR_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    cur: int
    max: int
    def __init__(self, cur: _Optional[int] = ..., max: _Optional[int] = ...) -> None: ...
