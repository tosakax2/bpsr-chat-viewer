from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotClaimedReward(_message.Message):
    __slots__ = ("award_time", "award_id_list")
    AWARD_TIME_FIELD_NUMBER: _ClassVar[int]
    AWARD_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    award_time: int
    award_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, award_time: _Optional[int] = ..., award_id_list: _Optional[_Iterable[int]] = ...) -> None: ...
