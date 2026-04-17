from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TowerJumpAward(_message.Message):
    __slots__ = ("climb_up_id",)
    CLIMB_UP_ID_FIELD_NUMBER: _ClassVar[int]
    climb_up_id: int
    def __init__(self, climb_up_id: _Optional[int] = ...) -> None: ...
