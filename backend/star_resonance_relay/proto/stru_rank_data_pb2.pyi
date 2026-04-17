from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RankData(_message.Message):
    __slots__ = ("rank", "char_id", "score")
    RANK_FIELD_NUMBER: _ClassVar[int]
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    rank: int
    char_id: int
    score: int
    def __init__(self, rank: _Optional[int] = ..., char_id: _Optional[int] = ..., score: _Optional[int] = ...) -> None: ...
