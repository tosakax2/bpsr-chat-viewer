import stru_user_activity_reward_info_pb2 as _stru_user_activity_reward_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserActivityInfo(_message.Message):
    __slots__ = ("start_time", "end_time", "rewards")
    class RewardsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_user_activity_reward_info_pb2.UserActivityRewardInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_user_activity_reward_info_pb2.UserActivityRewardInfo, _Mapping]] = ...) -> None: ...
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    REWARDS_FIELD_NUMBER: _ClassVar[int]
    start_time: int
    end_time: int
    rewards: _containers.MessageMap[int, _stru_user_activity_reward_info_pb2.UserActivityRewardInfo]
    def __init__(self, start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., rewards: _Optional[_Mapping[int, _stru_user_activity_reward_info_pb2.UserActivityRewardInfo]] = ...) -> None: ...
