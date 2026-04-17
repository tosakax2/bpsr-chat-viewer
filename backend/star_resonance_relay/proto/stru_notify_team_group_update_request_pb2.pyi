import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_team_member_group_info_pb2 as _stru_team_member_group_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyTeamGroupUpdateRequest(_message.Message):
    __slots__ = ("err_code", "team_member_group_infos")
    class TeamMemberGroupInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_team_member_group_info_pb2.TeamMemberGroupInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_team_member_group_info_pb2.TeamMemberGroupInfo, _Mapping]] = ...) -> None: ...
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    TEAM_MEMBER_GROUP_INFOS_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    team_member_group_infos: _containers.MessageMap[int, _stru_team_member_group_info_pb2.TeamMemberGroupInfo]
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., team_member_group_infos: _Optional[_Mapping[int, _stru_team_member_group_info_pb2.TeamMemberGroupInfo]] = ...) -> None: ...
