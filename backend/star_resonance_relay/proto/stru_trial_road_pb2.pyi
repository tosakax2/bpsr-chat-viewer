import stru_trial_road_room_target_award_pb2 as _stru_trial_road_room_target_award_pb2
import stru_trial_road_target_award_pb2 as _stru_trial_road_target_award_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrialRoad(_message.Message):
    __slots__ = ("pass_room", "room_target_award", "target_award")
    class RoomTargetAwardEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_trial_road_room_target_award_pb2.TrialRoadRoomTargetAward
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_trial_road_room_target_award_pb2.TrialRoadRoomTargetAward, _Mapping]] = ...) -> None: ...
    PASS_ROOM_FIELD_NUMBER: _ClassVar[int]
    ROOM_TARGET_AWARD_FIELD_NUMBER: _ClassVar[int]
    TARGET_AWARD_FIELD_NUMBER: _ClassVar[int]
    pass_room: _containers.RepeatedScalarFieldContainer[int]
    room_target_award: _containers.MessageMap[int, _stru_trial_road_room_target_award_pb2.TrialRoadRoomTargetAward]
    target_award: _stru_trial_road_target_award_pb2.TrialRoadTargetAward
    def __init__(self, pass_room: _Optional[_Iterable[int]] = ..., room_target_award: _Optional[_Mapping[int, _stru_trial_road_room_target_award_pb2.TrialRoadRoomTargetAward]] = ..., target_award: _Optional[_Union[_stru_trial_road_target_award_pb2.TrialRoadTargetAward, _Mapping]] = ...) -> None: ...
