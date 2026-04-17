from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WorldQuestInfo(_message.Message):
    __slots__ = ("finish_points", "rewards", "exceeding_points")
    FINISH_POINTS_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    EXCEEDING_POINTS_FIELD_NUMBER: _ClassVar[int]
    finish_points: int
    rewards: _containers.RepeatedScalarFieldContainer[int]
    exceeding_points: int
    def __init__(self, finish_points: _Optional[int] = ..., rewards: _Optional[_Iterable[int]] = ..., exceeding_points: _Optional[int] = ...) -> None: ...
