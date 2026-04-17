import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_show_team_pb2 as _stru_show_team_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetTeamListReply(_message.Message):
    __slots__ = ("target_id", "team_list", "is_refresh", "member_count", "ignore_self_talent", "err_code")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_LIST_FIELD_NUMBER: _ClassVar[int]
    IS_REFRESH_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    IGNORE_SELF_TALENT_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    target_id: int
    team_list: _containers.RepeatedCompositeFieldContainer[_stru_show_team_pb2.ShowTeam]
    is_refresh: bool
    member_count: int
    ignore_self_talent: bool
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, target_id: _Optional[int] = ..., team_list: _Optional[_Iterable[_Union[_stru_show_team_pb2.ShowTeam, _Mapping]]] = ..., is_refresh: bool = ..., member_count: _Optional[int] = ..., ignore_self_talent: bool = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
