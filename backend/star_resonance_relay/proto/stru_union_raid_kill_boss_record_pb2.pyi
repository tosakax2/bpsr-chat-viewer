from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnionRaidKillBossRecord(_message.Message):
    __slots__ = ("char_id", "char_name", "kill_time")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    CHAR_NAME_FIELD_NUMBER: _ClassVar[int]
    KILL_TIME_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    char_name: str
    kill_time: int
    def __init__(self, char_id: _Optional[int] = ..., char_name: _Optional[str] = ..., kill_time: _Optional[int] = ...) -> None: ...
