import stru_trial_road_target_progress_pb2 as _stru_trial_road_target_progress_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrialRoadTargetAward(_message.Message):
    __slots__ = ("target_progress",)
    class TargetProgressEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_trial_road_target_progress_pb2.TrialRoadTargetProgress
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_trial_road_target_progress_pb2.TrialRoadTargetProgress, _Mapping]] = ...) -> None: ...
    TARGET_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    target_progress: _containers.MessageMap[int, _stru_trial_road_target_progress_pb2.TrialRoadTargetProgress]
    def __init__(self, target_progress: _Optional[_Mapping[int, _stru_trial_road_target_progress_pb2.TrialRoadTargetProgress]] = ...) -> None: ...
