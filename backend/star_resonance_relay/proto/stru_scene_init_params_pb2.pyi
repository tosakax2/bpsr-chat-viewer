import stru_dungeon_hot_key_context_pb2 as _stru_dungeon_hot_key_context_pb2
import stru_dungeon_single_ai_mode_context_pb2 as _stru_dungeon_single_ai_mode_context_pb2
import stru_dungeon_union_info_pb2 as _stru_dungeon_union_info_pb2
import stru_homeland_info_pb2 as _stru_homeland_info_pb2
import stru_match_key_info_pb2 as _stru_match_key_info_pb2
import stru_planet_memory_context_pb2 as _stru_planet_memory_context_pb2
import stru_ride_seat_info_pb2 as _stru_ride_seat_info_pb2
import stru_weekly_tower_info_pb2 as _stru_weekly_tower_info_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneInitParams(_message.Message):
    __slots__ = ("owners", "change_flag", "context", "affixes", "team_id", "community_id", "homeland_id", "community_map_id", "homeland_info", "union_info", "single_ai_mode_context", "dungeon_hot_key_context", "scene_guid_index", "weekly_tower_info", "ride_seat_info", "init_params", "master_mode_diff", "match_key_info")
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    CHANGE_FLAG_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    AFFIXES_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    HOMELAND_ID_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_MAP_ID_FIELD_NUMBER: _ClassVar[int]
    HOMELAND_INFO_FIELD_NUMBER: _ClassVar[int]
    UNION_INFO_FIELD_NUMBER: _ClassVar[int]
    SINGLE_AI_MODE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_HOT_KEY_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SCENE_GUID_INDEX_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_TOWER_INFO_FIELD_NUMBER: _ClassVar[int]
    RIDE_SEAT_INFO_FIELD_NUMBER: _ClassVar[int]
    INIT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MASTER_MODE_DIFF_FIELD_NUMBER: _ClassVar[int]
    MATCH_KEY_INFO_FIELD_NUMBER: _ClassVar[int]
    owners: _containers.RepeatedScalarFieldContainer[int]
    change_flag: int
    context: _stru_planet_memory_context_pb2.PlanetMemoryContext
    affixes: _containers.RepeatedScalarFieldContainer[int]
    team_id: int
    community_id: int
    homeland_id: int
    community_map_id: int
    homeland_info: _stru_homeland_info_pb2.HomelandInfo
    union_info: _stru_dungeon_union_info_pb2.DungeonUnionInfo
    single_ai_mode_context: _stru_dungeon_single_ai_mode_context_pb2.DungeonSingleAiModeContext
    dungeon_hot_key_context: _stru_dungeon_hot_key_context_pb2.DungeonHotKeyContext
    scene_guid_index: str
    weekly_tower_info: _stru_weekly_tower_info_pb2.WeeklyTowerInfo
    ride_seat_info: _stru_ride_seat_info_pb2.RideSeatInfo
    init_params: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    master_mode_diff: int
    match_key_info: _stru_match_key_info_pb2.MatchKeyInfo
    def __init__(self, owners: _Optional[_Iterable[int]] = ..., change_flag: _Optional[int] = ..., context: _Optional[_Union[_stru_planet_memory_context_pb2.PlanetMemoryContext, _Mapping]] = ..., affixes: _Optional[_Iterable[int]] = ..., team_id: _Optional[int] = ..., community_id: _Optional[int] = ..., homeland_id: _Optional[int] = ..., community_map_id: _Optional[int] = ..., homeland_info: _Optional[_Union[_stru_homeland_info_pb2.HomelandInfo, _Mapping]] = ..., union_info: _Optional[_Union[_stru_dungeon_union_info_pb2.DungeonUnionInfo, _Mapping]] = ..., single_ai_mode_context: _Optional[_Union[_stru_dungeon_single_ai_mode_context_pb2.DungeonSingleAiModeContext, _Mapping]] = ..., dungeon_hot_key_context: _Optional[_Union[_stru_dungeon_hot_key_context_pb2.DungeonHotKeyContext, _Mapping]] = ..., scene_guid_index: _Optional[str] = ..., weekly_tower_info: _Optional[_Union[_stru_weekly_tower_info_pb2.WeeklyTowerInfo, _Mapping]] = ..., ride_seat_info: _Optional[_Union[_stru_ride_seat_info_pb2.RideSeatInfo, _Mapping]] = ..., init_params: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., master_mode_diff: _Optional[int] = ..., match_key_info: _Optional[_Union[_stru_match_key_info_pb2.MatchKeyInfo, _Mapping]] = ...) -> None: ...
