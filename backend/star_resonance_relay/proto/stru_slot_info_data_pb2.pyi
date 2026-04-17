from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SlotInfoData(_message.Message):
    __slots__ = ("id", "skill_id", "is_replace", "show_effect", "cd", "is_auto_battle_close")
    ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_REPLACE_FIELD_NUMBER: _ClassVar[int]
    SHOW_EFFECT_FIELD_NUMBER: _ClassVar[int]
    CD_FIELD_NUMBER: _ClassVar[int]
    IS_AUTO_BATTLE_CLOSE_FIELD_NUMBER: _ClassVar[int]
    id: int
    skill_id: int
    is_replace: bool
    show_effect: bool
    cd: int
    is_auto_battle_close: bool
    def __init__(self, id: _Optional[int] = ..., skill_id: _Optional[int] = ..., is_replace: bool = ..., show_effect: bool = ..., cd: _Optional[int] = ..., is_auto_battle_close: bool = ...) -> None: ...
