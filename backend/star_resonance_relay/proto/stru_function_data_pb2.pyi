from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FunctionData(_message.Message):
    __slots__ = ("unlocked_map", "drawn_function_ids")
    class UnlockedMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    UNLOCKED_MAP_FIELD_NUMBER: _ClassVar[int]
    DRAWN_FUNCTION_IDS_FIELD_NUMBER: _ClassVar[int]
    unlocked_map: _containers.ScalarMap[int, bool]
    drawn_function_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, unlocked_map: _Optional[_Mapping[int, bool]] = ..., drawn_function_ids: _Optional[_Iterable[int]] = ...) -> None: ...
