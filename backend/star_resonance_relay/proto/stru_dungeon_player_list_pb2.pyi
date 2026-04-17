import stru_dungeon_player_info_pb2 as _stru_dungeon_player_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonPlayerList(_message.Message):
    __slots__ = ("player_infos",)
    class PlayerInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_dungeon_player_info_pb2.DungeonPlayerInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_dungeon_player_info_pb2.DungeonPlayerInfo, _Mapping]] = ...) -> None: ...
    PLAYER_INFOS_FIELD_NUMBER: _ClassVar[int]
    player_infos: _containers.MessageMap[int, _stru_dungeon_player_info_pb2.DungeonPlayerInfo]
    def __init__(self, player_infos: _Optional[_Mapping[int, _stru_dungeon_player_info_pb2.DungeonPlayerInfo]] = ...) -> None: ...
