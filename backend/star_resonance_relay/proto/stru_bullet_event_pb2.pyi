from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BulletEvent(_message.Message):
    __slots__ = ("Uuid", "EnterStageId")
    UUID_FIELD_NUMBER: _ClassVar[int]
    ENTERSTAGEID_FIELD_NUMBER: _ClassVar[int]
    Uuid: int
    EnterStageId: int
    def __init__(self, Uuid: _Optional[int] = ..., EnterStageId: _Optional[int] = ...) -> None: ...
