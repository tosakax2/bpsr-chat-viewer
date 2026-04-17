from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonSceneInfo(_message.Message):
    __slots__ = ("difficulty",)
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    difficulty: int
    def __init__(self, difficulty: _Optional[int] = ...) -> None: ...
