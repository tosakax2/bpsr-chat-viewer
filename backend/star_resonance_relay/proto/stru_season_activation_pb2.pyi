import stru_season_activation_target_pb2 as _stru_season_activation_target_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonActivation(_message.Message):
    __slots__ = ("season_id", "activation_point", "refresh_time", "activation_targets", "stage_reward_status")
    class ActivationTargetsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_season_activation_target_pb2.SeasonActivationTarget
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_season_activation_target_pb2.SeasonActivationTarget, _Mapping]] = ...) -> None: ...
    class StageRewardStatusEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_POINT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_TARGETS_FIELD_NUMBER: _ClassVar[int]
    STAGE_REWARD_STATUS_FIELD_NUMBER: _ClassVar[int]
    season_id: int
    activation_point: int
    refresh_time: int
    activation_targets: _containers.MessageMap[int, _stru_season_activation_target_pb2.SeasonActivationTarget]
    stage_reward_status: _containers.ScalarMap[int, int]
    def __init__(self, season_id: _Optional[int] = ..., activation_point: _Optional[int] = ..., refresh_time: _Optional[int] = ..., activation_targets: _Optional[_Mapping[int, _stru_season_activation_target_pb2.SeasonActivationTarget]] = ..., stage_reward_status: _Optional[_Mapping[int, int]] = ...) -> None: ...
