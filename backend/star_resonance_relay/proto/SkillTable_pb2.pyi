import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkillTableBase(_message.Message):
    __slots__ = ("id", "name_design", "desc", "name", "skill_level_group", "effect_i_ds", "skill_type", "face_target", "is_preview", "target_type", "skill_target_range_type", "skill_range_type", "skill_select_point_type", "skill_hated_type", "skill_dam_type", "switch_skill_id", "is_aoe", "icon", "next_skill_id", "slot_type", "long_press_replace_s_kill_id", "long_press_time", "combo_take_effect_time", "can_play_in_sky", "sky_skill_id", "is_armor", "cant_stiff", "cant_stiff_back", "cant_stiff_down", "cant_stiff_air", "unbreak_skill_priority", "break_skill_priority", "use_total_damage_hud", "weapon_return", "skill_root_shift", "cool_time_type", "necessary_parts", "exclude_parts", "skill_area_array", "switch_skill_info", "energy_charge_time", "max_energy_charge_num", "continues_skill_delay_time", "use_add_res_value", "atk_speed_switch", "skill_look_at_angle", "defocus_look_atangle", "is_fracture_skill", "is_danger_skill", "is_passive_desc", "is_search_enemie", "search_enemie_filter_name", "rocker_dir", "skill_unbreak_level_additional", "is_hide_replace_effect", "change_wp_in_skill", "is_tanlent_continued_begin", "ui_warning_param", "inherit_motion_speed")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_DESIGN_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SKILL_LEVEL_GROUP_FIELD_NUMBER: _ClassVar[int]
    EFFECT_I_DS_FIELD_NUMBER: _ClassVar[int]
    SKILL_TYPE_FIELD_NUMBER: _ClassVar[int]
    FACE_TARGET_FIELD_NUMBER: _ClassVar[int]
    IS_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    SKILL_TARGET_RANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SKILL_RANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SKILL_SELECT_POINT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SKILL_HATED_TYPE_FIELD_NUMBER: _ClassVar[int]
    SKILL_DAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    SWITCH_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_AOE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    NEXT_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    SLOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    LONG_PRESS_REPLACE_S_KILL_ID_FIELD_NUMBER: _ClassVar[int]
    LONG_PRESS_TIME_FIELD_NUMBER: _ClassVar[int]
    COMBO_TAKE_EFFECT_TIME_FIELD_NUMBER: _ClassVar[int]
    CAN_PLAY_IN_SKY_FIELD_NUMBER: _ClassVar[int]
    SKY_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ARMOR_FIELD_NUMBER: _ClassVar[int]
    CANT_STIFF_FIELD_NUMBER: _ClassVar[int]
    CANT_STIFF_BACK_FIELD_NUMBER: _ClassVar[int]
    CANT_STIFF_DOWN_FIELD_NUMBER: _ClassVar[int]
    CANT_STIFF_AIR_FIELD_NUMBER: _ClassVar[int]
    UNBREAK_SKILL_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    BREAK_SKILL_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    USE_TOTAL_DAMAGE_HUD_FIELD_NUMBER: _ClassVar[int]
    WEAPON_RETURN_FIELD_NUMBER: _ClassVar[int]
    SKILL_ROOT_SHIFT_FIELD_NUMBER: _ClassVar[int]
    COOL_TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    NECESSARY_PARTS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_PARTS_FIELD_NUMBER: _ClassVar[int]
    SKILL_AREA_ARRAY_FIELD_NUMBER: _ClassVar[int]
    SWITCH_SKILL_INFO_FIELD_NUMBER: _ClassVar[int]
    ENERGY_CHARGE_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_ENERGY_CHARGE_NUM_FIELD_NUMBER: _ClassVar[int]
    CONTINUES_SKILL_DELAY_TIME_FIELD_NUMBER: _ClassVar[int]
    USE_ADD_RES_VALUE_FIELD_NUMBER: _ClassVar[int]
    ATK_SPEED_SWITCH_FIELD_NUMBER: _ClassVar[int]
    SKILL_LOOK_AT_ANGLE_FIELD_NUMBER: _ClassVar[int]
    DEFOCUS_LOOK_ATANGLE_FIELD_NUMBER: _ClassVar[int]
    IS_FRACTURE_SKILL_FIELD_NUMBER: _ClassVar[int]
    IS_DANGER_SKILL_FIELD_NUMBER: _ClassVar[int]
    IS_PASSIVE_DESC_FIELD_NUMBER: _ClassVar[int]
    IS_SEARCH_ENEMIE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ENEMIE_FILTER_NAME_FIELD_NUMBER: _ClassVar[int]
    ROCKER_DIR_FIELD_NUMBER: _ClassVar[int]
    SKILL_UNBREAK_LEVEL_ADDITIONAL_FIELD_NUMBER: _ClassVar[int]
    IS_HIDE_REPLACE_EFFECT_FIELD_NUMBER: _ClassVar[int]
    CHANGE_WP_IN_SKILL_FIELD_NUMBER: _ClassVar[int]
    IS_TANLENT_CONTINUED_BEGIN_FIELD_NUMBER: _ClassVar[int]
    UI_WARNING_PARAM_FIELD_NUMBER: _ClassVar[int]
    INHERIT_MOTION_SPEED_FIELD_NUMBER: _ClassVar[int]
    id: int
    name_design: str
    desc: _table_basic_pb2.mlstring
    name: _table_basic_pb2.mlstring
    skill_level_group: _table_basic_pb2.int_array
    effect_i_ds: _table_basic_pb2.int_array
    skill_type: int
    face_target: bool
    is_preview: bool
    target_type: int
    skill_target_range_type: int
    skill_range_type: int
    skill_select_point_type: int
    skill_hated_type: int
    skill_dam_type: int
    switch_skill_id: int
    is_aoe: bool
    icon: str
    next_skill_id: int
    slot_type: int
    long_press_replace_s_kill_id: int
    long_press_time: float
    combo_take_effect_time: float
    can_play_in_sky: bool
    sky_skill_id: int
    is_armor: bool
    cant_stiff: bool
    cant_stiff_back: bool
    cant_stiff_down: bool
    cant_stiff_air: bool
    unbreak_skill_priority: int
    break_skill_priority: int
    use_total_damage_hud: bool
    weapon_return: bool
    skill_root_shift: float
    cool_time_type: float
    necessary_parts: _table_basic_pb2.int_array
    exclude_parts: _table_basic_pb2.int_array
    skill_area_array: _table_basic_pb2.string_array
    switch_skill_info: _table_basic_pb2.number_table
    energy_charge_time: int
    max_energy_charge_num: int
    continues_skill_delay_time: float
    use_add_res_value: int
    atk_speed_switch: bool
    skill_look_at_angle: int
    defocus_look_atangle: int
    is_fracture_skill: bool
    is_danger_skill: bool
    is_passive_desc: bool
    is_search_enemie: bool
    search_enemie_filter_name: str
    rocker_dir: bool
    skill_unbreak_level_additional: int
    is_hide_replace_effect: bool
    change_wp_in_skill: bool
    is_tanlent_continued_begin: bool
    ui_warning_param: _table_basic_pb2.number_array
    inherit_motion_speed: bool
    def __init__(self, id: _Optional[int] = ..., name_design: _Optional[str] = ..., desc: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., skill_level_group: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., effect_i_ds: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., skill_type: _Optional[int] = ..., face_target: bool = ..., is_preview: bool = ..., target_type: _Optional[int] = ..., skill_target_range_type: _Optional[int] = ..., skill_range_type: _Optional[int] = ..., skill_select_point_type: _Optional[int] = ..., skill_hated_type: _Optional[int] = ..., skill_dam_type: _Optional[int] = ..., switch_skill_id: _Optional[int] = ..., is_aoe: bool = ..., icon: _Optional[str] = ..., next_skill_id: _Optional[int] = ..., slot_type: _Optional[int] = ..., long_press_replace_s_kill_id: _Optional[int] = ..., long_press_time: _Optional[float] = ..., combo_take_effect_time: _Optional[float] = ..., can_play_in_sky: bool = ..., sky_skill_id: _Optional[int] = ..., is_armor: bool = ..., cant_stiff: bool = ..., cant_stiff_back: bool = ..., cant_stiff_down: bool = ..., cant_stiff_air: bool = ..., unbreak_skill_priority: _Optional[int] = ..., break_skill_priority: _Optional[int] = ..., use_total_damage_hud: bool = ..., weapon_return: bool = ..., skill_root_shift: _Optional[float] = ..., cool_time_type: _Optional[float] = ..., necessary_parts: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., exclude_parts: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., skill_area_array: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., switch_skill_info: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., energy_charge_time: _Optional[int] = ..., max_energy_charge_num: _Optional[int] = ..., continues_skill_delay_time: _Optional[float] = ..., use_add_res_value: _Optional[int] = ..., atk_speed_switch: bool = ..., skill_look_at_angle: _Optional[int] = ..., defocus_look_atangle: _Optional[int] = ..., is_fracture_skill: bool = ..., is_danger_skill: bool = ..., is_passive_desc: bool = ..., is_search_enemie: bool = ..., search_enemie_filter_name: _Optional[str] = ..., rocker_dir: bool = ..., skill_unbreak_level_additional: _Optional[int] = ..., is_hide_replace_effect: bool = ..., change_wp_in_skill: bool = ..., is_tanlent_continued_begin: bool = ..., ui_warning_param: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., inherit_motion_speed: bool = ...) -> None: ...

class SkillTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SkillTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SkillTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SkillTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SkillTableBase]] = ...) -> None: ...
