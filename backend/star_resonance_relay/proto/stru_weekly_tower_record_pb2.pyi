from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WeeklyTowerRecord(_message.Message):
    __slots__ = ("begin_time", "max_climb_up_id", "award_climb_up_ids", "rule_id", "max_jump_award_climb_up_id", "last_max_climb_up_id")
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_CLIMB_UP_ID_FIELD_NUMBER: _ClassVar[int]
    AWARD_CLIMB_UP_IDS_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_JUMP_AWARD_CLIMB_UP_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_MAX_CLIMB_UP_ID_FIELD_NUMBER: _ClassVar[int]
    begin_time: int
    max_climb_up_id: int
    award_climb_up_ids: _containers.RepeatedScalarFieldContainer[int]
    rule_id: int
    max_jump_award_climb_up_id: int
    last_max_climb_up_id: int
    def __init__(self, begin_time: _Optional[int] = ..., max_climb_up_id: _Optional[int] = ..., award_climb_up_ids: _Optional[_Iterable[int]] = ..., rule_id: _Optional[int] = ..., max_jump_award_climb_up_id: _Optional[int] = ..., last_max_climb_up_id: _Optional[int] = ...) -> None: ...
