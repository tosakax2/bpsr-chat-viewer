from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonRankInfo(_message.Message):
    __slots__ = ("num", "rank")
    NUM_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    num: int
    rank: int
    def __init__(self, num: _Optional[int] = ..., rank: _Optional[int] = ...) -> None: ...
