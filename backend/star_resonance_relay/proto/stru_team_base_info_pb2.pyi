import enum_e_team_member_type_pb2 as _enum_e_team_member_type_pb2
import stru_team_member_group_info_pb2 as _stru_team_member_group_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TeamBaseInfo(_message.Message):
    __slots__ = ("team_id", "target_id", "leader_id", "desc", "auto_match", "hall_show", "matching", "team_member_type", "team_member_group_infos", "create_time")
    class TeamMemberGroupInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_team_member_group_info_pb2.TeamMemberGroupInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_team_member_group_info_pb2.TeamMemberGroupInfo, _Mapping]] = ...) -> None: ...
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    LEADER_ID_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    AUTO_MATCH_FIELD_NUMBER: _ClassVar[int]
    HALL_SHOW_FIELD_NUMBER: _ClassVar[int]
    MATCHING_FIELD_NUMBER: _ClassVar[int]
    TEAM_MEMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEAM_MEMBER_GROUP_INFOS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    target_id: int
    leader_id: int
    desc: str
    auto_match: bool
    hall_show: bool
    matching: bool
    team_member_type: _enum_e_team_member_type_pb2.ETeamMemberType
    team_member_group_infos: _containers.MessageMap[int, _stru_team_member_group_info_pb2.TeamMemberGroupInfo]
    create_time: int
    def __init__(self, team_id: _Optional[int] = ..., target_id: _Optional[int] = ..., leader_id: _Optional[int] = ..., desc: _Optional[str] = ..., auto_match: bool = ..., hall_show: bool = ..., matching: bool = ..., team_member_type: _Optional[_Union[_enum_e_team_member_type_pb2.ETeamMemberType, str]] = ..., team_member_group_infos: _Optional[_Mapping[int, _stru_team_member_group_info_pb2.TeamMemberGroupInfo]] = ..., create_time: _Optional[int] = ...) -> None: ...
