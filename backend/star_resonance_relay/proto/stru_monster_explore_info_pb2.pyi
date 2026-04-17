from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MonsterExploreInfo(_message.Message):
    __slots__ = ("is_unlock", "target_num", "award_flag", "is_flag")
    class TargetNumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    IS_UNLOCK_FIELD_NUMBER: _ClassVar[int]
    TARGET_NUM_FIELD_NUMBER: _ClassVar[int]
    AWARD_FLAG_FIELD_NUMBER: _ClassVar[int]
    IS_FLAG_FIELD_NUMBER: _ClassVar[int]
    is_unlock: bool
    target_num: _containers.ScalarMap[int, int]
    award_flag: int
    is_flag: bool
    def __init__(self, is_unlock: bool = ..., target_num: _Optional[_Mapping[int, int]] = ..., award_flag: _Optional[int] = ..., is_flag: bool = ...) -> None: ...
