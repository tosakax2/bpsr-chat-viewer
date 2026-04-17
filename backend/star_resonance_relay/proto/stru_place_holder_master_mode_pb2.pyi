import stru_master_mode_diff_dungeon_info_pb2 as _stru_master_mode_diff_dungeon_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlaceHolderMasterMode(_message.Message):
    __slots__ = ("master_mode_info", "user_name", "season_id")
    class MasterModeInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_master_mode_diff_dungeon_info_pb2.MasterModeDiffDungeonInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_master_mode_diff_dungeon_info_pb2.MasterModeDiffDungeonInfo, _Mapping]] = ...) -> None: ...
    MASTER_MODE_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    master_mode_info: _containers.MessageMap[int, _stru_master_mode_diff_dungeon_info_pb2.MasterModeDiffDungeonInfo]
    user_name: str
    season_id: int
    def __init__(self, master_mode_info: _Optional[_Mapping[int, _stru_master_mode_diff_dungeon_info_pb2.MasterModeDiffDungeonInfo]] = ..., user_name: _Optional[str] = ..., season_id: _Optional[int] = ...) -> None: ...
