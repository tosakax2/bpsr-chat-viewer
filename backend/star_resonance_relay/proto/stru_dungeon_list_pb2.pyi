import stru_dungeon_enter_limit_pb2 as _stru_dungeon_enter_limit_pb2
import stru_dungeon_info_pb2 as _stru_dungeon_info_pb2
import stru_dungeon_week_target_list_pb2 as _stru_dungeon_week_target_list_pb2
import stru_raid_record_pb2 as _stru_raid_record_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonList(_message.Message):
    __slots__ = ("complete_dungeon", "reset_time", "normal_dungeon_pass_count", "dungeon_enter_limit", "week_target", "is_assist", "raid_record_table")
    class CompleteDungeonEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_dungeon_info_pb2.DungeonInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_dungeon_info_pb2.DungeonInfo, _Mapping]] = ...) -> None: ...
    class RaidRecordTableEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_raid_record_pb2.RaidRecord
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_raid_record_pb2.RaidRecord, _Mapping]] = ...) -> None: ...
    COMPLETE_DUNGEON_FIELD_NUMBER: _ClassVar[int]
    RESET_TIME_FIELD_NUMBER: _ClassVar[int]
    NORMAL_DUNGEON_PASS_COUNT_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_ENTER_LIMIT_FIELD_NUMBER: _ClassVar[int]
    WEEK_TARGET_FIELD_NUMBER: _ClassVar[int]
    IS_ASSIST_FIELD_NUMBER: _ClassVar[int]
    RAID_RECORD_TABLE_FIELD_NUMBER: _ClassVar[int]
    complete_dungeon: _containers.MessageMap[int, _stru_dungeon_info_pb2.DungeonInfo]
    reset_time: int
    normal_dungeon_pass_count: int
    dungeon_enter_limit: _stru_dungeon_enter_limit_pb2.DungeonEnterLimit
    week_target: _stru_dungeon_week_target_list_pb2.DungeonWeekTargetList
    is_assist: bool
    raid_record_table: _containers.MessageMap[int, _stru_raid_record_pb2.RaidRecord]
    def __init__(self, complete_dungeon: _Optional[_Mapping[int, _stru_dungeon_info_pb2.DungeonInfo]] = ..., reset_time: _Optional[int] = ..., normal_dungeon_pass_count: _Optional[int] = ..., dungeon_enter_limit: _Optional[_Union[_stru_dungeon_enter_limit_pb2.DungeonEnterLimit, _Mapping]] = ..., week_target: _Optional[_Union[_stru_dungeon_week_target_list_pb2.DungeonWeekTargetList, _Mapping]] = ..., is_assist: bool = ..., raid_record_table: _Optional[_Mapping[int, _stru_raid_record_pb2.RaidRecord]] = ...) -> None: ...
