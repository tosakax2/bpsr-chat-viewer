from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RogueLockedEntry(_message.Message):
    __slots__ = ("id", "obj_uuid", "index")
    ID_FIELD_NUMBER: _ClassVar[int]
    OBJ_UUID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    id: int
    obj_uuid: int
    index: int
    def __init__(self, id: _Optional[int] = ..., obj_uuid: _Optional[int] = ..., index: _Optional[int] = ...) -> None: ...
