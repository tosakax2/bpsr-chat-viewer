from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChallengeAffixParam(_message.Message):
    __slots__ = ("dungeon_id", "diff")
    DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    DIFF_FIELD_NUMBER: _ClassVar[int]
    dungeon_id: int
    diff: int
    def __init__(self, dungeon_id: _Optional[int] = ..., diff: _Optional[int] = ...) -> None: ...
