from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MedalHole(_message.Message):
    __slots__ = ("hole_id", "hole_level", "cur_exp")
    HOLE_ID_FIELD_NUMBER: _ClassVar[int]
    HOLE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CUR_EXP_FIELD_NUMBER: _ClassVar[int]
    hole_id: int
    hole_level: int
    cur_exp: int
    def __init__(self, hole_id: _Optional[int] = ..., hole_level: _Optional[int] = ..., cur_exp: _Optional[int] = ...) -> None: ...
