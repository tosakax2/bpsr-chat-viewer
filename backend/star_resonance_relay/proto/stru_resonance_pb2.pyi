from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Resonance(_message.Message):
    __slots__ = ("resonances", "installed")
    class ResonancesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    RESONANCES_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_FIELD_NUMBER: _ClassVar[int]
    resonances: _containers.ScalarMap[int, int]
    installed: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, resonances: _Optional[_Mapping[int, int]] = ..., installed: _Optional[_Iterable[int]] = ...) -> None: ...
