from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LifeProfessionRDAlchemyReq(_message.Message):
    __slots__ = ("materials",)
    MATERIALS_FIELD_NUMBER: _ClassVar[int]
    materials: int
    def __init__(self, materials: _Optional[int] = ...) -> None: ...
