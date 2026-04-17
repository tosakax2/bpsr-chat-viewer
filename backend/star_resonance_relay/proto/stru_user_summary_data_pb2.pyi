import stru_avatar_info_pb2 as _stru_avatar_info_pb2
import stru_basic_data_pb2 as _stru_basic_data_pb2
import stru_char_team_pb2 as _stru_char_team_pb2
import stru_community_summary_data_pb2 as _stru_community_summary_data_pb2
import stru_privilege_data_pb2 as _stru_privilege_data_pb2
import stru_profession_data_pb2 as _stru_profession_data_pb2
import stru_union_data_pb2 as _stru_union_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserSummaryData(_message.Message):
    __slots__ = ("basic_data", "avatar_info", "profession_data", "fight_point", "team_data", "union_data", "community_data", "privilege_data")
    BASIC_DATA_FIELD_NUMBER: _ClassVar[int]
    AVATAR_INFO_FIELD_NUMBER: _ClassVar[int]
    PROFESSION_DATA_FIELD_NUMBER: _ClassVar[int]
    FIGHT_POINT_FIELD_NUMBER: _ClassVar[int]
    TEAM_DATA_FIELD_NUMBER: _ClassVar[int]
    UNION_DATA_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_DATA_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGE_DATA_FIELD_NUMBER: _ClassVar[int]
    basic_data: _stru_basic_data_pb2.BasicData
    avatar_info: _stru_avatar_info_pb2.AvatarInfo
    profession_data: _stru_profession_data_pb2.ProfessionData
    fight_point: int
    team_data: _stru_char_team_pb2.CharTeam
    union_data: _stru_union_data_pb2.UnionData
    community_data: _stru_community_summary_data_pb2.CommunitySummaryData
    privilege_data: _stru_privilege_data_pb2.PrivilegeData
    def __init__(self, basic_data: _Optional[_Union[_stru_basic_data_pb2.BasicData, _Mapping]] = ..., avatar_info: _Optional[_Union[_stru_avatar_info_pb2.AvatarInfo, _Mapping]] = ..., profession_data: _Optional[_Union[_stru_profession_data_pb2.ProfessionData, _Mapping]] = ..., fight_point: _Optional[int] = ..., team_data: _Optional[_Union[_stru_char_team_pb2.CharTeam, _Mapping]] = ..., union_data: _Optional[_Union[_stru_union_data_pb2.UnionData, _Mapping]] = ..., community_data: _Optional[_Union[_stru_community_summary_data_pb2.CommunitySummaryData, _Mapping]] = ..., privilege_data: _Optional[_Union[_stru_privilege_data_pb2.PrivilegeData, _Mapping]] = ...) -> None: ...
