from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReplaceSkillInfo(_message.Message):
    __slots__ = ("uuid", "begin_time", "skill_id", "replace_skill")
    UUID_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    REPLACE_SKILL_FIELD_NUMBER: _ClassVar[int]
    uuid: int
    begin_time: int
    skill_id: int
    replace_skill: int
    def __init__(self, uuid: _Optional[int] = ..., begin_time: _Optional[int] = ..., skill_id: _Optional[int] = ..., replace_skill: _Optional[int] = ...) -> None: ...
