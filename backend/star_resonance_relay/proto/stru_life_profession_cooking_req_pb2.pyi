from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LifeProfessionCookingReq(_message.Message):
    __slots__ = ("recipe_id", "count", "materials")
    RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    MATERIALS_FIELD_NUMBER: _ClassVar[int]
    recipe_id: int
    count: int
    materials: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, recipe_id: _Optional[int] = ..., count: _Optional[int] = ..., materials: _Optional[_Iterable[int]] = ...) -> None: ...
