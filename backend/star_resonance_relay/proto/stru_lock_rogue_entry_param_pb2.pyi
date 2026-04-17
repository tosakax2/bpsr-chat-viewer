from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LockRogueEntryParam(_message.Message):
    __slots__ = ("obj_uuid", "unlock", "index")
    OBJ_UUID_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    obj_uuid: int
    unlock: bool
    index: int
    def __init__(self, obj_uuid: _Optional[int] = ..., unlock: bool = ..., index: _Optional[int] = ...) -> None: ...
