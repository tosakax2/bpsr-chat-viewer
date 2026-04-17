import stru_union_dance_history_pb2 as _stru_union_dance_history_pb2
import stru_union_history_active_pb2 as _stru_union_history_active_pb2
import stru_user_union_hunt_info_pb2 as _stru_user_union_hunt_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserUnion(_message.Message):
    __slots__ = ("union_id", "next_join_time", "req_union_times", "join_flag", "collected_ids", "active_award_reset_time", "received_award_ids", "history_active_points", "active_last_refresh_time", "finish_daily_active_ids", "leave_time", "dance_record", "user_union_hunt_info")
    class ReqUnionTimesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_JOIN_TIME_FIELD_NUMBER: _ClassVar[int]
    REQ_UNION_TIMES_FIELD_NUMBER: _ClassVar[int]
    JOIN_FLAG_FIELD_NUMBER: _ClassVar[int]
    COLLECTED_IDS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_AWARD_RESET_TIME_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AWARD_IDS_FIELD_NUMBER: _ClassVar[int]
    HISTORY_ACTIVE_POINTS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_LAST_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    FINISH_DAILY_ACTIVE_IDS_FIELD_NUMBER: _ClassVar[int]
    LEAVE_TIME_FIELD_NUMBER: _ClassVar[int]
    DANCE_RECORD_FIELD_NUMBER: _ClassVar[int]
    USER_UNION_HUNT_INFO_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    next_join_time: int
    req_union_times: _containers.ScalarMap[int, int]
    join_flag: bool
    collected_ids: _containers.RepeatedScalarFieldContainer[int]
    active_award_reset_time: int
    received_award_ids: _containers.RepeatedScalarFieldContainer[int]
    history_active_points: _containers.RepeatedCompositeFieldContainer[_stru_union_history_active_pb2.UnionHistoryActive]
    active_last_refresh_time: int
    finish_daily_active_ids: _containers.RepeatedScalarFieldContainer[int]
    leave_time: int
    dance_record: _stru_union_dance_history_pb2.UnionDanceHistory
    user_union_hunt_info: _stru_user_union_hunt_info_pb2.UserUnionHuntInfo
    def __init__(self, union_id: _Optional[int] = ..., next_join_time: _Optional[int] = ..., req_union_times: _Optional[_Mapping[int, int]] = ..., join_flag: bool = ..., collected_ids: _Optional[_Iterable[int]] = ..., active_award_reset_time: _Optional[int] = ..., received_award_ids: _Optional[_Iterable[int]] = ..., history_active_points: _Optional[_Iterable[_Union[_stru_union_history_active_pb2.UnionHistoryActive, _Mapping]]] = ..., active_last_refresh_time: _Optional[int] = ..., finish_daily_active_ids: _Optional[_Iterable[int]] = ..., leave_time: _Optional[int] = ..., dance_record: _Optional[_Union[_stru_union_dance_history_pb2.UnionDanceHistory, _Mapping]] = ..., user_union_hunt_info: _Optional[_Union[_stru_user_union_hunt_info_pb2.UserUnionHuntInfo, _Mapping]] = ...) -> None: ...
