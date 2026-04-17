from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SkillSkin(_message.Message):
    __slots__ = ("skill_id", "skin_id")
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    SKIN_ID_FIELD_NUMBER: _ClassVar[int]
    skill_id: int
    skin_id: int
    def __init__(self, skill_id: _Optional[int] = ..., skin_id: _Optional[int] = ...) -> None: ...
