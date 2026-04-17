from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CultivateNormalNodeData(_message.Message):
    __slots__ = ("active_level",)
    ACTIVE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    active_level: int
    def __init__(self, active_level: _Optional[int] = ...) -> None: ...
