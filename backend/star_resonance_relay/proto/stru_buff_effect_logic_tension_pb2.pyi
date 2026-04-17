from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BuffEffectLogicTension(_message.Message):
    __slots__ = ("target_uuid", "strength", "strength_length", "max_length")
    TARGET_UUID_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    target_uuid: int
    strength: _containers.RepeatedScalarFieldContainer[int]
    strength_length: int
    max_length: int
    def __init__(self, target_uuid: _Optional[int] = ..., strength: _Optional[_Iterable[int]] = ..., strength_length: _Optional[int] = ..., max_length: _Optional[int] = ...) -> None: ...
