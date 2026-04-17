from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WorldBossRankInfo(_message.Message):
    __slots__ = ("char_id", "score")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    score: int
    def __init__(self, char_id: _Optional[int] = ..., score: _Optional[int] = ...) -> None: ...
