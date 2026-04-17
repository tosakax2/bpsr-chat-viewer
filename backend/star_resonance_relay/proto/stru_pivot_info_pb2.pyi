from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PivotInfo(_message.Message):
    __slots__ = ("id", "break_point", "reward_stage", "reward_full_state")
    ID_FIELD_NUMBER: _ClassVar[int]
    BREAK_POINT_FIELD_NUMBER: _ClassVar[int]
    REWARD_STAGE_FIELD_NUMBER: _ClassVar[int]
    REWARD_FULL_STATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    break_point: _containers.RepeatedScalarFieldContainer[int]
    reward_stage: _containers.RepeatedScalarFieldContainer[int]
    reward_full_state: int
    def __init__(self, id: _Optional[int] = ..., break_point: _Optional[_Iterable[int]] = ..., reward_stage: _Optional[_Iterable[int]] = ..., reward_full_state: _Optional[int] = ...) -> None: ...
