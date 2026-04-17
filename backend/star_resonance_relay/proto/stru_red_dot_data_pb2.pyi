from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RedDotData(_message.Message):
    __slots__ = ("permanent_closed_red_dot", "red_dot_count")
    class PermanentClosedRedDotEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class RedDotCountEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PERMANENT_CLOSED_RED_DOT_FIELD_NUMBER: _ClassVar[int]
    RED_DOT_COUNT_FIELD_NUMBER: _ClassVar[int]
    permanent_closed_red_dot: _containers.ScalarMap[int, bool]
    red_dot_count: _containers.ScalarMap[int, int]
    def __init__(self, permanent_closed_red_dot: _Optional[_Mapping[int, bool]] = ..., red_dot_count: _Optional[_Mapping[int, int]] = ...) -> None: ...
