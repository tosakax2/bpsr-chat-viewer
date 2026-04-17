import stru_dungeon_info_pb2 as _stru_dungeon_info_pb2
import stru_dungeon_target_award_pb2 as _stru_dungeon_target_award_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChallengeDungeonInfo(_message.Message):
    __slots__ = ("dungeon_info", "dungeon_target_award")
    class DungeonInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_dungeon_info_pb2.DungeonInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_dungeon_info_pb2.DungeonInfo, _Mapping]] = ...) -> None: ...
    class DungeonTargetAwardEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_dungeon_target_award_pb2.DungeonTargetAward
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_dungeon_target_award_pb2.DungeonTargetAward, _Mapping]] = ...) -> None: ...
    DUNGEON_INFO_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_TARGET_AWARD_FIELD_NUMBER: _ClassVar[int]
    dungeon_info: _containers.MessageMap[int, _stru_dungeon_info_pb2.DungeonInfo]
    dungeon_target_award: _containers.MessageMap[int, _stru_dungeon_target_award_pb2.DungeonTargetAward]
    def __init__(self, dungeon_info: _Optional[_Mapping[int, _stru_dungeon_info_pb2.DungeonInfo]] = ..., dungeon_target_award: _Optional[_Mapping[int, _stru_dungeon_target_award_pb2.DungeonTargetAward]] = ...) -> None: ...
