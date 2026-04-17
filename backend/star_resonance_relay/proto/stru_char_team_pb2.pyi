import enum_e_team_member_type_pb2 as _enum_e_team_member_type_pb2
import stru_team_mem_data_pb2 as _stru_team_mem_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CharTeam(_message.Message):
    __slots__ = ("team_id", "leader_id", "team_target_id", "team_num", "char_ids", "is_matching", "char_team_version", "team_member_data", "team_member_type")
    class TeamMemberDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_team_mem_data_pb2.TeamMemData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_team_mem_data_pb2.TeamMemData, _Mapping]] = ...) -> None: ...
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    LEADER_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_NUM_FIELD_NUMBER: _ClassVar[int]
    CHAR_IDS_FIELD_NUMBER: _ClassVar[int]
    IS_MATCHING_FIELD_NUMBER: _ClassVar[int]
    CHAR_TEAM_VERSION_FIELD_NUMBER: _ClassVar[int]
    TEAM_MEMBER_DATA_FIELD_NUMBER: _ClassVar[int]
    TEAM_MEMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    leader_id: int
    team_target_id: int
    team_num: int
    char_ids: _containers.RepeatedScalarFieldContainer[int]
    is_matching: bool
    char_team_version: int
    team_member_data: _containers.MessageMap[int, _stru_team_mem_data_pb2.TeamMemData]
    team_member_type: _enum_e_team_member_type_pb2.ETeamMemberType
    def __init__(self, team_id: _Optional[int] = ..., leader_id: _Optional[int] = ..., team_target_id: _Optional[int] = ..., team_num: _Optional[int] = ..., char_ids: _Optional[_Iterable[int]] = ..., is_matching: bool = ..., char_team_version: _Optional[int] = ..., team_member_data: _Optional[_Mapping[int, _stru_team_mem_data_pb2.TeamMemData]] = ..., team_member_type: _Optional[_Union[_enum_e_team_member_type_pb2.ETeamMemberType, str]] = ...) -> None: ...
