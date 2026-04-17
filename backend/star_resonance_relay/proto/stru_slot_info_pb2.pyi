from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SlotInfo(_message.Message):
    __slots__ = ("id", "skill_id", "is_auto_battle_close")
    ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_AUTO_BATTLE_CLOSE_FIELD_NUMBER: _ClassVar[int]
    id: int
    skill_id: int
    is_auto_battle_close: bool
    def __init__(self, id: _Optional[int] = ..., skill_id: _Optional[int] = ..., is_auto_battle_close: bool = ...) -> None: ...
