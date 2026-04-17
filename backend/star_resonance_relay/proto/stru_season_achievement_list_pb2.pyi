import stru_season_achievement_pb2 as _stru_season_achievement_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonAchievementList(_message.Message):
    __slots__ = ("season_achievement_list", "has_init_dones", "version")
    class SeasonAchievementListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_season_achievement_pb2.SeasonAchievement
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_season_achievement_pb2.SeasonAchievement, _Mapping]] = ...) -> None: ...
    class HasInitDonesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    SEASON_ACHIEVEMENT_LIST_FIELD_NUMBER: _ClassVar[int]
    HAS_INIT_DONES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    season_achievement_list: _containers.MessageMap[int, _stru_season_achievement_pb2.SeasonAchievement]
    has_init_dones: _containers.ScalarMap[int, bool]
    version: int
    def __init__(self, season_achievement_list: _Optional[_Mapping[int, _stru_season_achievement_pb2.SeasonAchievement]] = ..., has_init_dones: _Optional[_Mapping[int, bool]] = ..., version: _Optional[int] = ...) -> None: ...
