import stru_apply_time_pb2 as _stru_apply_time_pb2
import enum_e_team_member_type_pb2 as _enum_e_team_member_type_pb2
import stru_team_mem_data_pb2 as _stru_team_mem_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShowTeam(_message.Message):
    __slots__ = ("team_id", "leader_id", "target_id", "matching", "desc", "mems", "set_target_time", "apply_time_list", "team_member_type")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    LEADER_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    MATCHING_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    MEMS_FIELD_NUMBER: _ClassVar[int]
    SET_TARGET_TIME_FIELD_NUMBER: _ClassVar[int]
    APPLY_TIME_LIST_FIELD_NUMBER: _ClassVar[int]
    TEAM_MEMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    leader_id: int
    target_id: int
    matching: bool
    desc: str
    mems: _containers.RepeatedCompositeFieldContainer[_stru_team_mem_data_pb2.TeamMemData]
    set_target_time: int
    apply_time_list: _containers.RepeatedCompositeFieldContainer[_stru_apply_time_pb2.ApplyTime]
    team_member_type: _enum_e_team_member_type_pb2.ETeamMemberType
    def __init__(self, team_id: _Optional[int] = ..., leader_id: _Optional[int] = ..., target_id: _Optional[int] = ..., matching: bool = ..., desc: _Optional[str] = ..., mems: _Optional[_Iterable[_Union[_stru_team_mem_data_pb2.TeamMemData, _Mapping]]] = ..., set_target_time: _Optional[int] = ..., apply_time_list: _Optional[_Iterable[_Union[_stru_apply_time_pb2.ApplyTime, _Mapping]]] = ..., team_member_type: _Optional[_Union[_enum_e_team_member_type_pb2.ETeamMemberType, str]] = ...) -> None: ...
