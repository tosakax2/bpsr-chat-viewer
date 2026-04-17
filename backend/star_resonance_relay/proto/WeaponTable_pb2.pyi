import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WeaponTableBase(_message.Message):
    __slots__ = ("id", "name", "icon", "story", "intro", "talent", "element", "weapon_broke_extra_item", "weapon_star_extra_item", "weapon_skill_extra_item", "is_close", "common_skill_ids", "has_secondary", "model_id", "weapon_model_id", "timeline_id", "model_pos", "model_rot", "model", "anim_template", "mount", "mount_offset", "mount_rot", "weapon_idle", "skill_ids", "acquired_skill_ids", "weared_skill_ids", "skill_ids_video", "special_skill_ids", "sky_skill_id", "fight_res_template_id", "whack_skill_id", "whack_take_effect_time", "passive_skill_id", "spacing_distance", "change_weapon_action", "st_range", "st_angle", "st_sphere_range", "st_distance_weight", "st_angle_weight", "st_close_distance_threshold", "st_cancel_range", "st_check_end_time", "sup_target_effect_range", "lock_cancel_range", "focus_cancel_range", "focus_check_end_time", "battle_rush_max_charge_count", "battle_rush_charge_time", "dodge_start_time", "dodge_count_down", "rush_skill_id", "rush_break_time", "rush_anim_time", "rush_performance_buff", "dodge_client_buff", "rush_curve", "take_weapon_in_battle", "basic_hit_tag", "tags", "fightback_skill_ids", "passive_id", "dodge_invincible_time", "effect_switch", "battle_rush_origin_energy_cost", "create", "factor", "obtain_tips", "index")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    STORY_FIELD_NUMBER: _ClassVar[int]
    INTRO_FIELD_NUMBER: _ClassVar[int]
    TALENT_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    WEAPON_BROKE_EXTRA_ITEM_FIELD_NUMBER: _ClassVar[int]
    WEAPON_STAR_EXTRA_ITEM_FIELD_NUMBER: _ClassVar[int]
    WEAPON_SKILL_EXTRA_ITEM_FIELD_NUMBER: _ClassVar[int]
    IS_CLOSE_FIELD_NUMBER: _ClassVar[int]
    COMMON_SKILL_IDS_FIELD_NUMBER: _ClassVar[int]
    HAS_SECONDARY_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    WEAPON_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_POS_FIELD_NUMBER: _ClassVar[int]
    MODEL_ROT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    ANIM_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    MOUNT_FIELD_NUMBER: _ClassVar[int]
    MOUNT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    MOUNT_ROT_FIELD_NUMBER: _ClassVar[int]
    WEAPON_IDLE_FIELD_NUMBER: _ClassVar[int]
    SKILL_IDS_FIELD_NUMBER: _ClassVar[int]
    ACQUIRED_SKILL_IDS_FIELD_NUMBER: _ClassVar[int]
    WEARED_SKILL_IDS_FIELD_NUMBER: _ClassVar[int]
    SKILL_IDS_VIDEO_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_SKILL_IDS_FIELD_NUMBER: _ClassVar[int]
    SKY_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    FIGHT_RES_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    WHACK_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    WHACK_TAKE_EFFECT_TIME_FIELD_NUMBER: _ClassVar[int]
    PASSIVE_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    SPACING_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_WEAPON_ACTION_FIELD_NUMBER: _ClassVar[int]
    ST_RANGE_FIELD_NUMBER: _ClassVar[int]
    ST_ANGLE_FIELD_NUMBER: _ClassVar[int]
    ST_SPHERE_RANGE_FIELD_NUMBER: _ClassVar[int]
    ST_DISTANCE_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    ST_ANGLE_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    ST_CLOSE_DISTANCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ST_CANCEL_RANGE_FIELD_NUMBER: _ClassVar[int]
    ST_CHECK_END_TIME_FIELD_NUMBER: _ClassVar[int]
    SUP_TARGET_EFFECT_RANGE_FIELD_NUMBER: _ClassVar[int]
    LOCK_CANCEL_RANGE_FIELD_NUMBER: _ClassVar[int]
    FOCUS_CANCEL_RANGE_FIELD_NUMBER: _ClassVar[int]
    FOCUS_CHECK_END_TIME_FIELD_NUMBER: _ClassVar[int]
    BATTLE_RUSH_MAX_CHARGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    BATTLE_RUSH_CHARGE_TIME_FIELD_NUMBER: _ClassVar[int]
    DODGE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    DODGE_COUNT_DOWN_FIELD_NUMBER: _ClassVar[int]
    RUSH_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    RUSH_BREAK_TIME_FIELD_NUMBER: _ClassVar[int]
    RUSH_ANIM_TIME_FIELD_NUMBER: _ClassVar[int]
    RUSH_PERFORMANCE_BUFF_FIELD_NUMBER: _ClassVar[int]
    DODGE_CLIENT_BUFF_FIELD_NUMBER: _ClassVar[int]
    RUSH_CURVE_FIELD_NUMBER: _ClassVar[int]
    TAKE_WEAPON_IN_BATTLE_FIELD_NUMBER: _ClassVar[int]
    BASIC_HIT_TAG_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    FIGHTBACK_SKILL_IDS_FIELD_NUMBER: _ClassVar[int]
    PASSIVE_ID_FIELD_NUMBER: _ClassVar[int]
    DODGE_INVINCIBLE_TIME_FIELD_NUMBER: _ClassVar[int]
    EFFECT_SWITCH_FIELD_NUMBER: _ClassVar[int]
    BATTLE_RUSH_ORIGIN_ENERGY_COST_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    FACTOR_FIELD_NUMBER: _ClassVar[int]
    OBTAIN_TIPS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    icon: str
    story: _table_basic_pb2.mlstring
    intro: _table_basic_pb2.mlstring
    talent: _table_basic_pb2.int_array
    element: int
    weapon_broke_extra_item: _table_basic_pb2.int_table
    weapon_star_extra_item: _table_basic_pb2.int_table
    weapon_skill_extra_item: _table_basic_pb2.int_table
    is_close: bool
    common_skill_ids: _table_basic_pb2.int_array
    has_secondary: bool
    model_id: int
    weapon_model_id: _table_basic_pb2.int_array
    timeline_id: int
    model_pos: _table_basic_pb2.number_table
    model_rot: _table_basic_pb2.number_table
    model: _table_basic_pb2.string_array
    anim_template: str
    mount: _table_basic_pb2.string_table
    mount_offset: _table_basic_pb2.number_table
    mount_rot: _table_basic_pb2.number_table
    weapon_idle: _table_basic_pb2.string_table
    skill_ids: _table_basic_pb2.int_array
    acquired_skill_ids: _table_basic_pb2.int_array
    weared_skill_ids: _table_basic_pb2.int_table
    skill_ids_video: _table_basic_pb2.string_table
    special_skill_ids: _table_basic_pb2.int_table
    sky_skill_id: int
    fight_res_template_id: int
    whack_skill_id: int
    whack_take_effect_time: float
    passive_skill_id: int
    spacing_distance: float
    change_weapon_action: _table_basic_pb2.string_array
    st_range: float
    st_angle: float
    st_sphere_range: float
    st_distance_weight: float
    st_angle_weight: float
    st_close_distance_threshold: float
    st_cancel_range: float
    st_check_end_time: float
    sup_target_effect_range: float
    lock_cancel_range: float
    focus_cancel_range: float
    focus_check_end_time: float
    battle_rush_max_charge_count: int
    battle_rush_charge_time: float
    dodge_start_time: _table_basic_pb2.number_array
    dodge_count_down: float
    rush_skill_id: int
    rush_break_time: float
    rush_anim_time: _table_basic_pb2.number_array
    rush_performance_buff: _table_basic_pb2.int_array
    dodge_client_buff: _table_basic_pb2.int_array
    rush_curve: _table_basic_pb2.string_array
    take_weapon_in_battle: bool
    basic_hit_tag: int
    tags: _table_basic_pb2.int_array
    fightback_skill_ids: _table_basic_pb2.int_array
    passive_id: int
    dodge_invincible_time: float
    effect_switch: _table_basic_pb2.int_table
    battle_rush_origin_energy_cost: _table_basic_pb2.int_array
    create: int
    factor: int
    obtain_tips: int
    index: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., icon: _Optional[str] = ..., story: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., intro: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., talent: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., element: _Optional[int] = ..., weapon_broke_extra_item: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., weapon_star_extra_item: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., weapon_skill_extra_item: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., is_close: bool = ..., common_skill_ids: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., has_secondary: bool = ..., model_id: _Optional[int] = ..., weapon_model_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., timeline_id: _Optional[int] = ..., model_pos: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., model_rot: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., model: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., anim_template: _Optional[str] = ..., mount: _Optional[_Union[_table_basic_pb2.string_table, _Mapping]] = ..., mount_offset: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., mount_rot: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., weapon_idle: _Optional[_Union[_table_basic_pb2.string_table, _Mapping]] = ..., skill_ids: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., acquired_skill_ids: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., weared_skill_ids: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., skill_ids_video: _Optional[_Union[_table_basic_pb2.string_table, _Mapping]] = ..., special_skill_ids: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., sky_skill_id: _Optional[int] = ..., fight_res_template_id: _Optional[int] = ..., whack_skill_id: _Optional[int] = ..., whack_take_effect_time: _Optional[float] = ..., passive_skill_id: _Optional[int] = ..., spacing_distance: _Optional[float] = ..., change_weapon_action: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., st_range: _Optional[float] = ..., st_angle: _Optional[float] = ..., st_sphere_range: _Optional[float] = ..., st_distance_weight: _Optional[float] = ..., st_angle_weight: _Optional[float] = ..., st_close_distance_threshold: _Optional[float] = ..., st_cancel_range: _Optional[float] = ..., st_check_end_time: _Optional[float] = ..., sup_target_effect_range: _Optional[float] = ..., lock_cancel_range: _Optional[float] = ..., focus_cancel_range: _Optional[float] = ..., focus_check_end_time: _Optional[float] = ..., battle_rush_max_charge_count: _Optional[int] = ..., battle_rush_charge_time: _Optional[float] = ..., dodge_start_time: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., dodge_count_down: _Optional[float] = ..., rush_skill_id: _Optional[int] = ..., rush_break_time: _Optional[float] = ..., rush_anim_time: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., rush_performance_buff: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., dodge_client_buff: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., rush_curve: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., take_weapon_in_battle: bool = ..., basic_hit_tag: _Optional[int] = ..., tags: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., fightback_skill_ids: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., passive_id: _Optional[int] = ..., dodge_invincible_time: _Optional[float] = ..., effect_switch: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., battle_rush_origin_energy_cost: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., create: _Optional[int] = ..., factor: _Optional[int] = ..., obtain_tips: _Optional[int] = ..., index: _Optional[int] = ...) -> None: ...

class WeaponTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: WeaponTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[WeaponTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, WeaponTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, WeaponTableBase]] = ...) -> None: ...
