from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonScore(_message.Message):
    __slots__ = ("total_score", "cur_ratio")
    TOTAL_SCORE_FIELD_NUMBER: _ClassVar[int]
    CUR_RATIO_FIELD_NUMBER: _ClassVar[int]
    total_score: int
    cur_ratio: int
    def __init__(self, total_score: _Optional[int] = ..., cur_ratio: _Optional[int] = ...) -> None: ...
