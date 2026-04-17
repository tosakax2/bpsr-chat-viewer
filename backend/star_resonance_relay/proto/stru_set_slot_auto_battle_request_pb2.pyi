from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetSlotAutoBattleRequest(_message.Message):
    __slots__ = ("slots",)
    class SlotsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    slots: _containers.ScalarMap[int, bool]
    def __init__(self, slots: _Optional[_Mapping[int, bool]] = ...) -> None: ...
