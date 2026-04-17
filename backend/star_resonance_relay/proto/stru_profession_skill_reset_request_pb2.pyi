from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProfessionSkillResetRequest(_message.Message):
    __slots__ = ("profession_id",)
    PROFESSION_ID_FIELD_NUMBER: _ClassVar[int]
    profession_id: int
    def __init__(self, profession_id: _Optional[int] = ...) -> None: ...
