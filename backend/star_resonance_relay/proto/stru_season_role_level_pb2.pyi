from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonRoleLevel(_message.Message):
    __slots__ = ("level", "cur_level_exp")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CUR_LEVEL_EXP_FIELD_NUMBER: _ClassVar[int]
    level: int
    cur_level_exp: int
    def __init__(self, level: _Optional[int] = ..., cur_level_exp: _Optional[int] = ...) -> None: ...
