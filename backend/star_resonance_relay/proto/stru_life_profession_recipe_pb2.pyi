from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LifeProfessionRecipe(_message.Message):
    __slots__ = ("id", "unlock_time")
    ID_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    unlock_time: int
    def __init__(self, id: _Optional[int] = ..., unlock_time: _Optional[int] = ...) -> None: ...
