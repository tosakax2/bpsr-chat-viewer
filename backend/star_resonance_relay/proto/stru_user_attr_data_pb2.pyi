from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UserAttrData(_message.Message):
    __slots__ = ("state", "fight_point")
    STATE_FIELD_NUMBER: _ClassVar[int]
    FIGHT_POINT_FIELD_NUMBER: _ClassVar[int]
    state: int
    fight_point: int
    def __init__(self, state: _Optional[int] = ..., fight_point: _Optional[int] = ...) -> None: ...
