import stru_assign_scene_params_pb2 as _stru_assign_scene_params_pb2
import enum_e_team_activity_state_pb2 as _enum_e_team_activity_state_pb2
import stru_team_activity_dungeon_info_pb2 as _stru_team_activity_dungeon_info_pb2
import stru_team_dungeon_key_info_pb2 as _stru_team_dungeon_key_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TeamActivity(_message.Message):
    __slots__ = ("activity_id", "state", "time", "dungeon_info", "agree_mem", "check_members", "refuse_id", "assign_scene_params", "award_count_info")
    class AwardCountInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_team_dungeon_key_info_pb2.TeamDungeonKeyInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_team_dungeon_key_info_pb2.TeamDungeonKeyInfo, _Mapping]] = ...) -> None: ...
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_INFO_FIELD_NUMBER: _ClassVar[int]
    AGREE_MEM_FIELD_NUMBER: _ClassVar[int]
    CHECK_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    REFUSE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_SCENE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AWARD_COUNT_INFO_FIELD_NUMBER: _ClassVar[int]
    activity_id: int
    state: _enum_e_team_activity_state_pb2.ETeamActivityState
    time: int
    dungeon_info: _stru_team_activity_dungeon_info_pb2.TeamActivityDungeonInfo
    agree_mem: _containers.RepeatedScalarFieldContainer[int]
    check_members: _containers.RepeatedScalarFieldContainer[int]
    refuse_id: int
    assign_scene_params: _stru_assign_scene_params_pb2.AssignSceneParams
    award_count_info: _containers.MessageMap[int, _stru_team_dungeon_key_info_pb2.TeamDungeonKeyInfo]
    def __init__(self, activity_id: _Optional[int] = ..., state: _Optional[_Union[_enum_e_team_activity_state_pb2.ETeamActivityState, str]] = ..., time: _Optional[int] = ..., dungeon_info: _Optional[_Union[_stru_team_activity_dungeon_info_pb2.TeamActivityDungeonInfo, _Mapping]] = ..., agree_mem: _Optional[_Iterable[int]] = ..., check_members: _Optional[_Iterable[int]] = ..., refuse_id: _Optional[int] = ..., assign_scene_params: _Optional[_Union[_stru_assign_scene_params_pb2.AssignSceneParams, _Mapping]] = ..., award_count_info: _Optional[_Mapping[int, _stru_team_dungeon_key_info_pb2.TeamDungeonKeyInfo]] = ...) -> None: ...
