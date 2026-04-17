from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlanetMemory(_message.Message):
    __slots__ = ("pass_room",)
    PASS_ROOM_FIELD_NUMBER: _ClassVar[int]
    pass_room: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, pass_room: _Optional[_Iterable[int]] = ...) -> None: ...
