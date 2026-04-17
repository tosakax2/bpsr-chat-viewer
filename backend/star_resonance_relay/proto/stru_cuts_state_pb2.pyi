from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CutsState(_message.Message):
    __slots__ = ("state_info",)
    class StateInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    STATE_INFO_FIELD_NUMBER: _ClassVar[int]
    state_info: _containers.ScalarMap[int, int]
    def __init__(self, state_info: _Optional[_Mapping[int, int]] = ...) -> None: ...
