import stru_dungeon_target_progress_pb2 as _stru_dungeon_target_progress_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonTargetAward(_message.Message):
    __slots__ = ("dungeon_target_progress",)
    class DungeonTargetProgressEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_dungeon_target_progress_pb2.DungeonTargetProgress
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_dungeon_target_progress_pb2.DungeonTargetProgress, _Mapping]] = ...) -> None: ...
    DUNGEON_TARGET_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    dungeon_target_progress: _containers.MessageMap[int, _stru_dungeon_target_progress_pb2.DungeonTargetProgress]
    def __init__(self, dungeon_target_progress: _Optional[_Mapping[int, _stru_dungeon_target_progress_pb2.DungeonTargetProgress]] = ...) -> None: ...
