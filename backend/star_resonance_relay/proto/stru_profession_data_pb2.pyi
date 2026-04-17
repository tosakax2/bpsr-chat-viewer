from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProfessionData(_message.Message):
    __slots__ = ("profession_id", "weapon_skin")
    PROFESSION_ID_FIELD_NUMBER: _ClassVar[int]
    WEAPON_SKIN_FIELD_NUMBER: _ClassVar[int]
    profession_id: int
    weapon_skin: int
    def __init__(self, profession_id: _Optional[int] = ..., weapon_skin: _Optional[int] = ...) -> None: ...
