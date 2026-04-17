from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LifeProfessionTargetInfo(_message.Message):
    __slots__ = ("id", "value", "level", "life_target_reward_states")
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    LIFE_TARGET_REWARD_STATES_FIELD_NUMBER: _ClassVar[int]
    id: int
    value: int
    level: int
    life_target_reward_states: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., value: _Optional[int] = ..., level: _Optional[int] = ..., life_target_reward_states: _Optional[_Iterable[int]] = ...) -> None: ...
