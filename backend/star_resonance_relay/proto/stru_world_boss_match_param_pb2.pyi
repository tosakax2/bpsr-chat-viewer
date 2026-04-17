from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WorldBossMatchParam(_message.Message):
    __slots__ = ("activity_id",)
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    activity_id: int
    def __init__(self, activity_id: _Optional[int] = ...) -> None: ...
