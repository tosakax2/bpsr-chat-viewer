import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_match_key_info_pb2 as _stru_match_key_info_pb2
import stru_match_player_info_pb2 as _stru_match_player_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MatchReadyStatusNtfRequest(_message.Message):
    __slots__ = ("err_code", "leader_char_id", "match_token", "match_key_info", "match_player_info")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    LEADER_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MATCH_KEY_INFO_FIELD_NUMBER: _ClassVar[int]
    MATCH_PLAYER_INFO_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    leader_char_id: int
    match_token: str
    match_key_info: _stru_match_key_info_pb2.MatchKeyInfo
    match_player_info: _containers.RepeatedCompositeFieldContainer[_stru_match_player_info_pb2.MatchPlayerInfo]
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., leader_char_id: _Optional[int] = ..., match_token: _Optional[str] = ..., match_key_info: _Optional[_Union[_stru_match_key_info_pb2.MatchKeyInfo, _Mapping]] = ..., match_player_info: _Optional[_Iterable[_Union[_stru_match_player_info_pb2.MatchPlayerInfo, _Mapping]]] = ...) -> None: ...
