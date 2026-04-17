import stru_match_player_show_info_pb2 as _stru_match_player_show_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerMahjongData(_message.Message):
    __slots__ = ("player_id", "is_robot", "match_player_show_info")
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ROBOT_FIELD_NUMBER: _ClassVar[int]
    MATCH_PLAYER_SHOW_INFO_FIELD_NUMBER: _ClassVar[int]
    player_id: int
    is_robot: bool
    match_player_show_info: _stru_match_player_show_info_pb2.MatchPlayerShowInfo
    def __init__(self, player_id: _Optional[int] = ..., is_robot: bool = ..., match_player_show_info: _Optional[_Union[_stru_match_player_show_info_pb2.MatchPlayerShowInfo, _Mapping]] = ...) -> None: ...
