from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UpgradeRogueEntryParam(_message.Message):
    __slots__ = ("obj_uuid", "id")
    OBJ_UUID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    obj_uuid: int
    id: int
    def __init__(self, obj_uuid: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...
