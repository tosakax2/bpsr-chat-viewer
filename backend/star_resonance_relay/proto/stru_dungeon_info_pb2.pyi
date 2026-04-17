from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonInfo(_message.Message):
    __slots__ = ("dungeon_id", "complete_count", "award_flg", "score", "pass_time")
    DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_COUNT_FIELD_NUMBER: _ClassVar[int]
    AWARD_FLG_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    PASS_TIME_FIELD_NUMBER: _ClassVar[int]
    dungeon_id: int
    complete_count: int
    award_flg: int
    score: int
    pass_time: int
    def __init__(self, dungeon_id: _Optional[int] = ..., complete_count: _Optional[int] = ..., award_flg: _Optional[int] = ..., score: _Optional[int] = ..., pass_time: _Optional[int] = ...) -> None: ...
