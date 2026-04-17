import stru_master_mode_diff_dungeon_info_pb2 as _stru_master_mode_diff_dungeon_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonMasterModeDungeonInfo(_message.Message):
    __slots__ = ("master_mode_diff_info", "dungeon_info_update_time", "season_awards")
    class MasterModeDiffInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_master_mode_diff_dungeon_info_pb2.MasterModeDiffDungeonInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_master_mode_diff_dungeon_info_pb2.MasterModeDiffDungeonInfo, _Mapping]] = ...) -> None: ...
    class SeasonAwardsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    MASTER_MODE_DIFF_INFO_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_INFO_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SEASON_AWARDS_FIELD_NUMBER: _ClassVar[int]
    master_mode_diff_info: _containers.MessageMap[int, _stru_master_mode_diff_dungeon_info_pb2.MasterModeDiffDungeonInfo]
    dungeon_info_update_time: int
    season_awards: _containers.ScalarMap[int, int]
    def __init__(self, master_mode_diff_info: _Optional[_Mapping[int, _stru_master_mode_diff_dungeon_info_pb2.MasterModeDiffDungeonInfo]] = ..., dungeon_info_update_time: _Optional[int] = ..., season_awards: _Optional[_Mapping[int, int]] = ...) -> None: ...
