from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MapStickerTaskInfo(_message.Message):
    __slots__ = ("task_id", "target_num")
    class TargetNumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_NUM_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    target_num: _containers.ScalarMap[int, int]
    def __init__(self, task_id: _Optional[int] = ..., target_num: _Optional[_Mapping[int, int]] = ...) -> None: ...
