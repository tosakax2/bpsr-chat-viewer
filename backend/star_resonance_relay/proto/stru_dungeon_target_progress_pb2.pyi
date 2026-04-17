from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonTargetProgress(_message.Message):
    __slots__ = ("target_id", "target_progress", "award_state")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    AWARD_STATE_FIELD_NUMBER: _ClassVar[int]
    target_id: int
    target_progress: int
    award_state: int
    def __init__(self, target_id: _Optional[int] = ..., target_progress: _Optional[int] = ..., award_state: _Optional[int] = ...) -> None: ...
