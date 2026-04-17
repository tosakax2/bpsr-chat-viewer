from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ShapeshiftSkill(_message.Message):
    __slots__ = ("index", "skill_id")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    index: int
    skill_id: int
    def __init__(self, index: _Optional[int] = ..., skill_id: _Optional[int] = ...) -> None: ...
