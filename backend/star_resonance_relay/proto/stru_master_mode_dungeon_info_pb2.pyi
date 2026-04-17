import stru_season_master_mode_dungeon_info_pb2 as _stru_season_master_mode_dungeon_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MasterModeDungeonInfo(_message.Message):
    __slots__ = ("master_mode_dungeon_info", "is_show", "cur_show_season")
    class MasterModeDungeonInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_season_master_mode_dungeon_info_pb2.SeasonMasterModeDungeonInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_season_master_mode_dungeon_info_pb2.SeasonMasterModeDungeonInfo, _Mapping]] = ...) -> None: ...
    MASTER_MODE_DUNGEON_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_FIELD_NUMBER: _ClassVar[int]
    CUR_SHOW_SEASON_FIELD_NUMBER: _ClassVar[int]
    master_mode_dungeon_info: _containers.MessageMap[int, _stru_season_master_mode_dungeon_info_pb2.SeasonMasterModeDungeonInfo]
    is_show: bool
    cur_show_season: int
    def __init__(self, master_mode_dungeon_info: _Optional[_Mapping[int, _stru_season_master_mode_dungeon_info_pb2.SeasonMasterModeDungeonInfo]] = ..., is_show: bool = ..., cur_show_season: _Optional[int] = ...) -> None: ...
