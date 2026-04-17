import stru_union_activity_target_pb2 as _stru_union_activity_target_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnionActivity(_message.Message):
    __slots__ = ("last_refresh_time", "union_targets", "next_award_time", "next_refresh_time", "reset_history_active_points", "cur_point")
    class UnionTargetsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_union_activity_target_pb2.UnionActivityTarget
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_union_activity_target_pb2.UnionActivityTarget, _Mapping]] = ...) -> None: ...
    class NextRefreshTimeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class ResetHistoryActivePointsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    LAST_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    UNION_TARGETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_AWARD_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    RESET_HISTORY_ACTIVE_POINTS_FIELD_NUMBER: _ClassVar[int]
    CUR_POINT_FIELD_NUMBER: _ClassVar[int]
    last_refresh_time: int
    union_targets: _containers.MessageMap[int, _stru_union_activity_target_pb2.UnionActivityTarget]
    next_award_time: int
    next_refresh_time: _containers.ScalarMap[int, int]
    reset_history_active_points: _containers.ScalarMap[int, int]
    cur_point: int
    def __init__(self, last_refresh_time: _Optional[int] = ..., union_targets: _Optional[_Mapping[int, _stru_union_activity_target_pb2.UnionActivityTarget]] = ..., next_award_time: _Optional[int] = ..., next_refresh_time: _Optional[_Mapping[int, int]] = ..., reset_history_active_points: _Optional[_Mapping[int, int]] = ..., cur_point: _Optional[int] = ...) -> None: ...
