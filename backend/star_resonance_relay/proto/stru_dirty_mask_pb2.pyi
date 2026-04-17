from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DirtyMask(_message.Message):
    __slots__ = ("dirty_key",)
    DIRTY_KEY_FIELD_NUMBER: _ClassVar[int]
    dirty_key: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, dirty_key: _Optional[_Iterable[int]] = ...) -> None: ...
