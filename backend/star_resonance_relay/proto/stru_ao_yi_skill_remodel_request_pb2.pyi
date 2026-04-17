from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AoYiSkillRemodelRequest(_message.Message):
    __slots__ = ("aoyi_star_id",)
    AOYI_STAR_ID_FIELD_NUMBER: _ClassVar[int]
    aoyi_star_id: int
    def __init__(self, aoyi_star_id: _Optional[int] = ...) -> None: ...
