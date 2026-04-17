from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonDungeonAffix(_message.Message):
    __slots__ = ("affixes",)
    AFFIXES_FIELD_NUMBER: _ClassVar[int]
    affixes: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, affixes: _Optional[_Iterable[int]] = ...) -> None: ...
