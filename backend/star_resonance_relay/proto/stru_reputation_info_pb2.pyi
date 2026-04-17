from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReputationInfo(_message.Message):
    __slots__ = ("reputation_exp", "reputation_level", "award_map")
    class AwardMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    REPUTATION_EXP_FIELD_NUMBER: _ClassVar[int]
    REPUTATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    AWARD_MAP_FIELD_NUMBER: _ClassVar[int]
    reputation_exp: int
    reputation_level: int
    award_map: _containers.ScalarMap[int, bool]
    def __init__(self, reputation_exp: _Optional[int] = ..., reputation_level: _Optional[int] = ..., award_map: _Optional[_Mapping[int, bool]] = ...) -> None: ...
