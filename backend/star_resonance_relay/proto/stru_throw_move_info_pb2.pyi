from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ThrowMoveInfo(_message.Message):
    __slots__ = ("target_uuid", "skill_id", "skill_level", "stage_id", "event_id")
    TARGET_UUID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    target_uuid: int
    skill_id: int
    skill_level: int
    stage_id: int
    event_id: int
    def __init__(self, target_uuid: _Optional[int] = ..., skill_id: _Optional[int] = ..., skill_level: _Optional[int] = ..., stage_id: _Optional[int] = ..., event_id: _Optional[int] = ...) -> None: ...
