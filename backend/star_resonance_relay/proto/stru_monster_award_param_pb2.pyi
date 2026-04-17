from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MonsterAwardParam(_message.Message):
    __slots__ = ("monster_id", "stage_id")
    MONSTER_ID_FIELD_NUMBER: _ClassVar[int]
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    monster_id: int
    stage_id: int
    def __init__(self, monster_id: _Optional[int] = ..., stage_id: _Optional[int] = ...) -> None: ...
