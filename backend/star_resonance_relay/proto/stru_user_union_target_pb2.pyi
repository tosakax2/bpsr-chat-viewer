import stru_user_union_target_info_pb2 as _stru_user_union_target_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserUnionTarget(_message.Message):
    __slots__ = ("is_init", "user_union_target_info", "week_target_reward_ids", "week_target_refresh_time")
    class UserUnionTargetInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_user_union_target_info_pb2.UserUnionTargetInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_user_union_target_info_pb2.UserUnionTargetInfo, _Mapping]] = ...) -> None: ...
    class WeekTargetRewardIdsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    IS_INIT_FIELD_NUMBER: _ClassVar[int]
    USER_UNION_TARGET_INFO_FIELD_NUMBER: _ClassVar[int]
    WEEK_TARGET_REWARD_IDS_FIELD_NUMBER: _ClassVar[int]
    WEEK_TARGET_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    is_init: int
    user_union_target_info: _containers.MessageMap[int, _stru_user_union_target_info_pb2.UserUnionTargetInfo]
    week_target_reward_ids: _containers.ScalarMap[int, int]
    week_target_refresh_time: int
    def __init__(self, is_init: _Optional[int] = ..., user_union_target_info: _Optional[_Mapping[int, _stru_user_union_target_info_pb2.UserUnionTargetInfo]] = ..., week_target_reward_ids: _Optional[_Mapping[int, int]] = ..., week_target_refresh_time: _Optional[int] = ...) -> None: ...
