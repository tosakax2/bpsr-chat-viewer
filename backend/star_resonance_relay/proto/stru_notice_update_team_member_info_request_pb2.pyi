import stru_team_member_fast_sync_data_pb2 as _stru_team_member_fast_sync_data_pb2
import stru_team_mem_data_pb2 as _stru_team_mem_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NoticeUpdateTeamMemberInfoRequest(_message.Message):
    __slots__ = ("team_member_sync_datas", "team_member_social_datas")
    TEAM_MEMBER_SYNC_DATAS_FIELD_NUMBER: _ClassVar[int]
    TEAM_MEMBER_SOCIAL_DATAS_FIELD_NUMBER: _ClassVar[int]
    team_member_sync_datas: _containers.RepeatedCompositeFieldContainer[_stru_team_member_fast_sync_data_pb2.TeamMemberFastSyncData]
    team_member_social_datas: _containers.RepeatedCompositeFieldContainer[_stru_team_mem_data_pb2.TeamMemData]
    def __init__(self, team_member_sync_datas: _Optional[_Iterable[_Union[_stru_team_member_fast_sync_data_pb2.TeamMemberFastSyncData, _Mapping]]] = ..., team_member_social_datas: _Optional[_Iterable[_Union[_stru_team_mem_data_pb2.TeamMemData, _Mapping]]] = ...) -> None: ...
