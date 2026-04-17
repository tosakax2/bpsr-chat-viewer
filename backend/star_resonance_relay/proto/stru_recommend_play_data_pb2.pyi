import enum_e_timer_exe_type_pb2 as _enum_e_timer_exe_type_pb2
import enum_e_timer_type_pb2 as _enum_e_timer_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecommendPlayData(_message.Message):
    __slots__ = ("start_timestamp", "end_timestamp", "is_open", "last_time_stamp", "last_end_time_stamp", "next_time_stamp", "next_end_time_stamp", "cur_type", "timer_type")
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IS_OPEN_FIELD_NUMBER: _ClassVar[int]
    LAST_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    LAST_END_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    NEXT_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    NEXT_END_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    CUR_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMER_TYPE_FIELD_NUMBER: _ClassVar[int]
    start_timestamp: int
    end_timestamp: int
    is_open: bool
    last_time_stamp: int
    last_end_time_stamp: int
    next_time_stamp: int
    next_end_time_stamp: int
    cur_type: _enum_e_timer_exe_type_pb2.ETimerExeType
    timer_type: _enum_e_timer_type_pb2.ETimerType
    def __init__(self, start_timestamp: _Optional[int] = ..., end_timestamp: _Optional[int] = ..., is_open: bool = ..., last_time_stamp: _Optional[int] = ..., last_end_time_stamp: _Optional[int] = ..., next_time_stamp: _Optional[int] = ..., next_end_time_stamp: _Optional[int] = ..., cur_type: _Optional[_Union[_enum_e_timer_exe_type_pb2.ETimerExeType, str]] = ..., timer_type: _Optional[_Union[_enum_e_timer_type_pb2.ETimerType, str]] = ...) -> None: ...
