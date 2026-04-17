import enum_e_match_mode_pb2 as _enum_e_match_mode_pb2
import enum_e_match_strategy_pb2 as _enum_e_match_strategy_pb2
import stru_match_key_info_pb2 as _stru_match_key_info_pb2
import stru_match_player_info_pb2 as _stru_match_player_info_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MatchParamContext(_message.Message):
    __slots__ = ("match_mode", "match_token", "team_id", "match_strategy", "match_strategy_param", "match_key_info", "match_grain_key", "match_player_info", "dungeon_id")
    MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    MATCH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    MATCH_STRATEGY_PARAM_FIELD_NUMBER: _ClassVar[int]
    MATCH_KEY_INFO_FIELD_NUMBER: _ClassVar[int]
    MATCH_GRAIN_KEY_FIELD_NUMBER: _ClassVar[int]
    MATCH_PLAYER_INFO_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    match_mode: _enum_e_match_mode_pb2.EMatchMode
    match_token: str
    team_id: int
    match_strategy: _enum_e_match_strategy_pb2.EMatchStrategy
    match_strategy_param: _any_pb2.Any
    match_key_info: _stru_match_key_info_pb2.MatchKeyInfo
    match_grain_key: str
    match_player_info: _stru_match_player_info_pb2.MatchPlayerInfo
    dungeon_id: int
    def __init__(self, match_mode: _Optional[_Union[_enum_e_match_mode_pb2.EMatchMode, str]] = ..., match_token: _Optional[str] = ..., team_id: _Optional[int] = ..., match_strategy: _Optional[_Union[_enum_e_match_strategy_pb2.EMatchStrategy, str]] = ..., match_strategy_param: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., match_key_info: _Optional[_Union[_stru_match_key_info_pb2.MatchKeyInfo, _Mapping]] = ..., match_grain_key: _Optional[str] = ..., match_player_info: _Optional[_Union[_stru_match_player_info_pb2.MatchPlayerInfo, _Mapping]] = ..., dungeon_id: _Optional[int] = ...) -> None: ...
