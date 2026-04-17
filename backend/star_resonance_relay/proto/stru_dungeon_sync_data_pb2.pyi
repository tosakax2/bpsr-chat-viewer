import stru_dungeon_affix_data_pb2 as _stru_dungeon_affix_data_pb2
import stru_dungeon_area_info_pb2 as _stru_dungeon_area_info_pb2
import stru_dungeon_damage_pb2 as _stru_dungeon_damage_pb2
import stru_dungeon_event_pb2 as _stru_dungeon_event_pb2
import stru_dungeon_flow_info_pb2 as _stru_dungeon_flow_info_pb2
import stru_dungeon_hero_key_info_pb2 as _stru_dungeon_hero_key_info_pb2
import stru_dungeon_pioneer_pb2 as _stru_dungeon_pioneer_pb2
import stru_dungeon_planet_memory_room_pb2 as _stru_dungeon_planet_memory_room_pb2
import stru_dungeon_player_list_pb2 as _stru_dungeon_player_list_pb2
import stru_dungeon_raid_info_pb2 as _stru_dungeon_raid_info_pb2
import stru_dungeon_random_entity_config_id_info_pb2 as _stru_dungeon_random_entity_config_id_info_pb2
import stru_dungeon_rank_list_pb2 as _stru_dungeon_rank_list_pb2
import stru_dungeon_revive_info_pb2 as _stru_dungeon_revive_info_pb2
import stru_dungeon_scene_info_pb2 as _stru_dungeon_scene_info_pb2
import stru_dungeon_score_pb2 as _stru_dungeon_score_pb2
import stru_dungeon_settlement_pb2 as _stru_dungeon_settlement_pb2
import stru_dungeon_target_pb2 as _stru_dungeon_target_pb2
import stru_dungeon_timer_info_pb2 as _stru_dungeon_timer_info_pb2
import stru_dungeon_title_pb2 as _stru_dungeon_title_pb2
import stru_dungeon_union_info_pb2 as _stru_dungeon_union_info_pb2
import stru_dungeon_var_pb2 as _stru_dungeon_var_pb2
import stru_dungeon_var_all_pb2 as _stru_dungeon_var_all_pb2
import stru_dungeon_vote_pb2 as _stru_dungeon_vote_pb2
import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonSyncData(_message.Message):
    __slots__ = ("scene_uuid", "flow_info", "title", "target", "damage", "vote", "settlement", "dungeon_pioneer", "planet_room_info", "dungeon_var", "dungeon_rank", "dungeon_affix_data", "dungeon_event", "dungeon_score", "timer_info", "hero_key", "dungeon_union_info", "dungeon_player_list", "revive_info", "random_entity_config_id_info", "dungeon_scene_info", "dungeon_var_all", "dungeon_raid_info", "dungeon_area_info", "err_code")
    SCENE_UUID_FIELD_NUMBER: _ClassVar[int]
    FLOW_INFO_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    DAMAGE_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    SETTLEMENT_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_PIONEER_FIELD_NUMBER: _ClassVar[int]
    PLANET_ROOM_INFO_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_VAR_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_RANK_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_AFFIX_DATA_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_EVENT_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_SCORE_FIELD_NUMBER: _ClassVar[int]
    TIMER_INFO_FIELD_NUMBER: _ClassVar[int]
    HERO_KEY_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_UNION_INFO_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_PLAYER_LIST_FIELD_NUMBER: _ClassVar[int]
    REVIVE_INFO_FIELD_NUMBER: _ClassVar[int]
    RANDOM_ENTITY_CONFIG_ID_INFO_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_SCENE_INFO_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_VAR_ALL_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_RAID_INFO_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_AREA_INFO_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    scene_uuid: int
    flow_info: _stru_dungeon_flow_info_pb2.DungeonFlowInfo
    title: _stru_dungeon_title_pb2.DungeonTitle
    target: _stru_dungeon_target_pb2.DungeonTarget
    damage: _stru_dungeon_damage_pb2.DungeonDamage
    vote: _stru_dungeon_vote_pb2.DungeonVote
    settlement: _stru_dungeon_settlement_pb2.DungeonSettlement
    dungeon_pioneer: _stru_dungeon_pioneer_pb2.DungeonPioneer
    planet_room_info: _stru_dungeon_planet_memory_room_pb2.DungeonPlanetMemoryRoom
    dungeon_var: _stru_dungeon_var_pb2.DungeonVar
    dungeon_rank: _stru_dungeon_rank_list_pb2.DungeonRankList
    dungeon_affix_data: _stru_dungeon_affix_data_pb2.DungeonAffixData
    dungeon_event: _stru_dungeon_event_pb2.DungeonEvent
    dungeon_score: _stru_dungeon_score_pb2.DungeonScore
    timer_info: _stru_dungeon_timer_info_pb2.DungeonTimerInfo
    hero_key: _stru_dungeon_hero_key_info_pb2.DungeonHeroKeyInfo
    dungeon_union_info: _stru_dungeon_union_info_pb2.DungeonUnionInfo
    dungeon_player_list: _stru_dungeon_player_list_pb2.DungeonPlayerList
    revive_info: _stru_dungeon_revive_info_pb2.DungeonReviveInfo
    random_entity_config_id_info: _stru_dungeon_random_entity_config_id_info_pb2.DungeonRandomEntityConfigIdInfo
    dungeon_scene_info: _stru_dungeon_scene_info_pb2.DungeonSceneInfo
    dungeon_var_all: _stru_dungeon_var_all_pb2.DungeonVarAll
    dungeon_raid_info: _stru_dungeon_raid_info_pb2.DungeonRaidInfo
    dungeon_area_info: _stru_dungeon_area_info_pb2.DungeonAreaInfo
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, scene_uuid: _Optional[int] = ..., flow_info: _Optional[_Union[_stru_dungeon_flow_info_pb2.DungeonFlowInfo, _Mapping]] = ..., title: _Optional[_Union[_stru_dungeon_title_pb2.DungeonTitle, _Mapping]] = ..., target: _Optional[_Union[_stru_dungeon_target_pb2.DungeonTarget, _Mapping]] = ..., damage: _Optional[_Union[_stru_dungeon_damage_pb2.DungeonDamage, _Mapping]] = ..., vote: _Optional[_Union[_stru_dungeon_vote_pb2.DungeonVote, _Mapping]] = ..., settlement: _Optional[_Union[_stru_dungeon_settlement_pb2.DungeonSettlement, _Mapping]] = ..., dungeon_pioneer: _Optional[_Union[_stru_dungeon_pioneer_pb2.DungeonPioneer, _Mapping]] = ..., planet_room_info: _Optional[_Union[_stru_dungeon_planet_memory_room_pb2.DungeonPlanetMemoryRoom, _Mapping]] = ..., dungeon_var: _Optional[_Union[_stru_dungeon_var_pb2.DungeonVar, _Mapping]] = ..., dungeon_rank: _Optional[_Union[_stru_dungeon_rank_list_pb2.DungeonRankList, _Mapping]] = ..., dungeon_affix_data: _Optional[_Union[_stru_dungeon_affix_data_pb2.DungeonAffixData, _Mapping]] = ..., dungeon_event: _Optional[_Union[_stru_dungeon_event_pb2.DungeonEvent, _Mapping]] = ..., dungeon_score: _Optional[_Union[_stru_dungeon_score_pb2.DungeonScore, _Mapping]] = ..., timer_info: _Optional[_Union[_stru_dungeon_timer_info_pb2.DungeonTimerInfo, _Mapping]] = ..., hero_key: _Optional[_Union[_stru_dungeon_hero_key_info_pb2.DungeonHeroKeyInfo, _Mapping]] = ..., dungeon_union_info: _Optional[_Union[_stru_dungeon_union_info_pb2.DungeonUnionInfo, _Mapping]] = ..., dungeon_player_list: _Optional[_Union[_stru_dungeon_player_list_pb2.DungeonPlayerList, _Mapping]] = ..., revive_info: _Optional[_Union[_stru_dungeon_revive_info_pb2.DungeonReviveInfo, _Mapping]] = ..., random_entity_config_id_info: _Optional[_Union[_stru_dungeon_random_entity_config_id_info_pb2.DungeonRandomEntityConfigIdInfo, _Mapping]] = ..., dungeon_scene_info: _Optional[_Union[_stru_dungeon_scene_info_pb2.DungeonSceneInfo, _Mapping]] = ..., dungeon_var_all: _Optional[_Union[_stru_dungeon_var_all_pb2.DungeonVarAll, _Mapping]] = ..., dungeon_raid_info: _Optional[_Union[_stru_dungeon_raid_info_pb2.DungeonRaidInfo, _Mapping]] = ..., dungeon_area_info: _Optional[_Union[_stru_dungeon_area_info_pb2.DungeonAreaInfo, _Mapping]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
