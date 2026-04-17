from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BubbleInfo(_message.Message):
    __slots__ = ("bubble_score", "bubble_award_count", "additional_target_uuid_list", "last_refresh_time")
    BUBBLE_SCORE_FIELD_NUMBER: _ClassVar[int]
    BUBBLE_AWARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_TARGET_UUID_LIST_FIELD_NUMBER: _ClassVar[int]
    LAST_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    bubble_score: int
    bubble_award_count: int
    additional_target_uuid_list: _containers.RepeatedScalarFieldContainer[int]
    last_refresh_time: int
    def __init__(self, bubble_score: _Optional[int] = ..., bubble_award_count: _Optional[int] = ..., additional_target_uuid_list: _Optional[_Iterable[int]] = ..., last_refresh_time: _Optional[int] = ...) -> None: ...
