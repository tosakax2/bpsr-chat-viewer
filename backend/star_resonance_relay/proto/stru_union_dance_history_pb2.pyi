from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnionDanceHistory(_message.Message):
    __slots__ = ("dance_end_time", "sent_dance_award", "drawn_dance_award")
    DANCE_END_TIME_FIELD_NUMBER: _ClassVar[int]
    SENT_DANCE_AWARD_FIELD_NUMBER: _ClassVar[int]
    DRAWN_DANCE_AWARD_FIELD_NUMBER: _ClassVar[int]
    dance_end_time: int
    sent_dance_award: bool
    drawn_dance_award: bool
    def __init__(self, dance_end_time: _Optional[int] = ..., sent_dance_award: bool = ..., drawn_dance_award: bool = ...) -> None: ...
