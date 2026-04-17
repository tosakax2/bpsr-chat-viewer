import stru_dungeon_target_progress_pb2 as _stru_dungeon_target_progress_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonWeekTargetList(_message.Message):
    __slots__ = ("week_target", "refresh_time")
    class WeekTargetEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_dungeon_target_progress_pb2.DungeonTargetProgress
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_dungeon_target_progress_pb2.DungeonTargetProgress, _Mapping]] = ...) -> None: ...
    WEEK_TARGET_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    week_target: _containers.MessageMap[int, _stru_dungeon_target_progress_pb2.DungeonTargetProgress]
    refresh_time: int
    def __init__(self, week_target: _Optional[_Mapping[int, _stru_dungeon_target_progress_pb2.DungeonTargetProgress]] = ..., refresh_time: _Optional[int] = ...) -> None: ...
