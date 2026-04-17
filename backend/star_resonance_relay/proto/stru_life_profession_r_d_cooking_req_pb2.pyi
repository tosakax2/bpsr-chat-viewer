from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LifeProfessionRDCookingReq(_message.Message):
    __slots__ = ("materials",)
    MATERIALS_FIELD_NUMBER: _ClassVar[int]
    materials: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, materials: _Optional[_Iterable[int]] = ...) -> None: ...
