from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnionGetKillBossDataRequest(_message.Message):
    __slots__ = ("union_id", "boss_id")
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    BOSS_ID_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    boss_id: int
    def __init__(self, union_id: _Optional[int] = ..., boss_id: _Optional[int] = ...) -> None: ...
