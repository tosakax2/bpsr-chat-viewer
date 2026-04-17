from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetFlagInfo(_message.Message):
    __slots__ = ("monster_id", "is_flag")
    MONSTER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_FLAG_FIELD_NUMBER: _ClassVar[int]
    monster_id: int
    is_flag: bool
    def __init__(self, monster_id: _Optional[int] = ..., is_flag: bool = ...) -> None: ...
