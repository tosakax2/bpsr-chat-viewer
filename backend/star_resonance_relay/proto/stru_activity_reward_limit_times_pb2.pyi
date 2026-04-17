import enum_e_timer_type_pb2 as _enum_e_timer_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivityRewardLimitTimes(_message.Message):
    __slots__ = ("times_type", "times", "max_times")
    TIMES_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMES_FIELD_NUMBER: _ClassVar[int]
    MAX_TIMES_FIELD_NUMBER: _ClassVar[int]
    times_type: _enum_e_timer_type_pb2.ETimerType
    times: int
    max_times: int
    def __init__(self, times_type: _Optional[_Union[_enum_e_timer_type_pb2.ETimerType, str]] = ..., times: _Optional[int] = ..., max_times: _Optional[int] = ...) -> None: ...
