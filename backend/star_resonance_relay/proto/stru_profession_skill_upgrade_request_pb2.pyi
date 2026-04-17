from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProfessionSkillUpgradeRequest(_message.Message):
    __slots__ = ("profession_id", "skill_id", "target_level")
    PROFESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_LEVEL_FIELD_NUMBER: _ClassVar[int]
    profession_id: int
    skill_id: int
    target_level: int
    def __init__(self, profession_id: _Optional[int] = ..., skill_id: _Optional[int] = ..., target_level: _Optional[int] = ...) -> None: ...
