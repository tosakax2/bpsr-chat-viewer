import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import enum_e_match_status_pb2 as _enum_e_match_status_pb2
import stru_match_key_info_pb2 as _stru_match_key_info_pb2
import stru_match_player_info_pb2 as _stru_match_player_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MatchInfo(_message.Message):
    __slots__ = ("match_status", "match_time", "match_player_info", "match_token", "match_ready_time", "match_key_info", "match_grain_key", "err_code")
    class MatchPlayerInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_match_player_info_pb2.MatchPlayerInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_match_player_info_pb2.MatchPlayerInfo, _Mapping]] = ...) -> None: ...
    MATCH_STATUS_FIELD_NUMBER: _ClassVar[int]
    MATCH_TIME_FIELD_NUMBER: _ClassVar[int]
    MATCH_PLAYER_INFO_FIELD_NUMBER: _ClassVar[int]
    MATCH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MATCH_READY_TIME_FIELD_NUMBER: _ClassVar[int]
    MATCH_KEY_INFO_FIELD_NUMBER: _ClassVar[int]
    MATCH_GRAIN_KEY_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    match_status: _enum_e_match_status_pb2.EMatchStatus
    match_time: int
    match_player_info: _containers.MessageMap[int, _stru_match_player_info_pb2.MatchPlayerInfo]
    match_token: str
    match_ready_time: int
    match_key_info: _stru_match_key_info_pb2.MatchKeyInfo
    match_grain_key: str
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, match_status: _Optional[_Union[_enum_e_match_status_pb2.EMatchStatus, str]] = ..., match_time: _Optional[int] = ..., match_player_info: _Optional[_Mapping[int, _stru_match_player_info_pb2.MatchPlayerInfo]] = ..., match_token: _Optional[str] = ..., match_ready_time: _Optional[int] = ..., match_key_info: _Optional[_Union[_stru_match_key_info_pb2.MatchKeyInfo, _Mapping]] = ..., match_grain_key: _Optional[str] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
