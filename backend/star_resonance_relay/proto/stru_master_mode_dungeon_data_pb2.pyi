from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MasterModeDungeonData(_message.Message):
    __slots__ = ("season_score", "is_show")
    SEASON_SCORE_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_FIELD_NUMBER: _ClassVar[int]
    season_score: int
    is_show: bool
    def __init__(self, season_score: _Optional[int] = ..., is_show: bool = ...) -> None: ...
