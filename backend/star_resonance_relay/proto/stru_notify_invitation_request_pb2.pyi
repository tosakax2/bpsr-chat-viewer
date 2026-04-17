import enum_e_team_member_type_pb2 as _enum_e_team_member_type_pb2
import stru_user_summary_data_pb2 as _stru_user_summary_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyInvitationRequest(_message.Message):
    __slots__ = ("teamid", "target_id", "team_num", "invite_mem_data", "team_member_type")
    TEAMID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_NUM_FIELD_NUMBER: _ClassVar[int]
    INVITE_MEM_DATA_FIELD_NUMBER: _ClassVar[int]
    TEAM_MEMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    teamid: int
    target_id: int
    team_num: int
    invite_mem_data: _stru_user_summary_data_pb2.UserSummaryData
    team_member_type: _enum_e_team_member_type_pb2.ETeamMemberType
    def __init__(self, teamid: _Optional[int] = ..., target_id: _Optional[int] = ..., team_num: _Optional[int] = ..., invite_mem_data: _Optional[_Union[_stru_user_summary_data_pb2.UserSummaryData, _Mapping]] = ..., team_member_type: _Optional[_Union[_enum_e_team_member_type_pb2.ETeamMemberType, str]] = ...) -> None: ...
