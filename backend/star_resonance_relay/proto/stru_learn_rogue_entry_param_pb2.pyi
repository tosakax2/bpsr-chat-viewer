from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LearnRogueEntryParam(_message.Message):
    __slots__ = ("obj_uuid", "index", "in_locked")
    OBJ_UUID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    IN_LOCKED_FIELD_NUMBER: _ClassVar[int]
    obj_uuid: int
    index: int
    in_locked: bool
    def __init__(self, obj_uuid: _Optional[int] = ..., index: _Optional[int] = ..., in_locked: bool = ...) -> None: ...
