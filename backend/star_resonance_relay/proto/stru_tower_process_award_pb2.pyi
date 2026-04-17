from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TowerProcessAward(_message.Message):
    __slots__ = ("climb_up_id", "one_key")
    CLIMB_UP_ID_FIELD_NUMBER: _ClassVar[int]
    ONE_KEY_FIELD_NUMBER: _ClassVar[int]
    climb_up_id: int
    one_key: bool
    def __init__(self, climb_up_id: _Optional[int] = ..., one_key: bool = ...) -> None: ...
