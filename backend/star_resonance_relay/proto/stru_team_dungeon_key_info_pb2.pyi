from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TeamDungeonKeyInfo(_message.Message):
    __slots__ = ("char_id", "roll_award_count", "key_award_count", "is_assist")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    ROLL_AWARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    KEY_AWARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_ASSIST_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    roll_award_count: int
    key_award_count: int
    is_assist: bool
    def __init__(self, char_id: _Optional[int] = ..., roll_award_count: _Optional[int] = ..., key_award_count: _Optional[int] = ..., is_assist: bool = ...) -> None: ...
