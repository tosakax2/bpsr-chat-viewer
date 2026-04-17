from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StructureMaterialInfo(_message.Message):
    __slots__ = ("material_id", "char_id")
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    material_id: int
    char_id: int
    def __init__(self, material_id: _Optional[int] = ..., char_id: _Optional[int] = ...) -> None: ...
