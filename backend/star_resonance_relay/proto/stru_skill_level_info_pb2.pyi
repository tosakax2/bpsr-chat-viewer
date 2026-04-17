from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SkillLevelInfo(_message.Message):
    __slots__ = ("skill_id", "current_level", "remodel_level")
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    REMODEL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    skill_id: int
    current_level: int
    remodel_level: int
    def __init__(self, skill_id: _Optional[int] = ..., current_level: _Optional[int] = ..., remodel_level: _Optional[int] = ...) -> None: ...
