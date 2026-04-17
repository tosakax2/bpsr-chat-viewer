import stru_home_land_task_pb2 as _stru_home_land_task_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeLandPlayerTaskInfo(_message.Message):
    __slots__ = ("next_task_reflush_time", "cur_left_times", "cur_task_map", "new_next_task_reflush_sec")
    class CurTaskMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_home_land_task_pb2.HomeLandTask
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_home_land_task_pb2.HomeLandTask, _Mapping]] = ...) -> None: ...
    NEXT_TASK_REFLUSH_TIME_FIELD_NUMBER: _ClassVar[int]
    CUR_LEFT_TIMES_FIELD_NUMBER: _ClassVar[int]
    CUR_TASK_MAP_FIELD_NUMBER: _ClassVar[int]
    NEW_NEXT_TASK_REFLUSH_SEC_FIELD_NUMBER: _ClassVar[int]
    next_task_reflush_time: int
    cur_left_times: int
    cur_task_map: _containers.MessageMap[int, _stru_home_land_task_pb2.HomeLandTask]
    new_next_task_reflush_sec: int
    def __init__(self, next_task_reflush_time: _Optional[int] = ..., cur_left_times: _Optional[int] = ..., cur_task_map: _Optional[_Mapping[int, _stru_home_land_task_pb2.HomeLandTask]] = ..., new_next_task_reflush_sec: _Optional[int] = ...) -> None: ...
