import stru_achievement_pb2 as _stru_achievement_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonAchievement(_message.Message):
    __slots__ = ("season_achievement",)
    class SeasonAchievementEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_achievement_pb2.Achievement
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_achievement_pb2.Achievement, _Mapping]] = ...) -> None: ...
    SEASON_ACHIEVEMENT_FIELD_NUMBER: _ClassVar[int]
    season_achievement: _containers.MessageMap[int, _stru_achievement_pb2.Achievement]
    def __init__(self, season_achievement: _Optional[_Mapping[int, _stru_achievement_pb2.Achievement]] = ...) -> None: ...
