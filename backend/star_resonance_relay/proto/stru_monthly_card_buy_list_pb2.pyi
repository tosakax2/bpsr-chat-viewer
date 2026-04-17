from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MonthlyCardBuyList(_message.Message):
    __slots__ = ("begin_time", "end_time", "last_award_day_time")
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_AWARD_DAY_TIME_FIELD_NUMBER: _ClassVar[int]
    begin_time: int
    end_time: int
    last_award_day_time: int
    def __init__(self, begin_time: _Optional[int] = ..., end_time: _Optional[int] = ..., last_award_day_time: _Optional[int] = ...) -> None: ...
