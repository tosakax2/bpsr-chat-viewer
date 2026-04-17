from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonRollParam(_message.Message):
    __slots__ = ("index", "give_up")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    GIVE_UP_FIELD_NUMBER: _ClassVar[int]
    index: int
    give_up: bool
    def __init__(self, index: _Optional[int] = ..., give_up: bool = ...) -> None: ...
