from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QuestHistory(_message.Message):
    __slots__ = ("step_history",)
    class StepHistoryEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    STEP_HISTORY_FIELD_NUMBER: _ClassVar[int]
    step_history: _containers.ScalarMap[int, int]
    def __init__(self, step_history: _Optional[_Mapping[int, int]] = ...) -> None: ...
