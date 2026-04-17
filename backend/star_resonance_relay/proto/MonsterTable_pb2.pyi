import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MonsterTableBase(_message.Message):
    __slots__ = ("id", "name", "model_id", "monster_type", "blood_tube_count", "comment1", "comment2", "skill_ids", "hatred_build_type", "is_flying", "sight_config", "is_accurate_sight", "hatred_away", "score", "hatred_away_type", "attribute_id", "walk_speed", "run_speed", "f_run_speed", "alert_speed", "min_alert_dis", "max_alert_dis", "export_voxel", "voxel_path", "default_camp", "is_show_hp", "entity_turn_velocity", "ai_table_reference", "attack_height", "drop_height", "dash_speed", "monster_fight_area", "hatred_away_show", "tags", "target_select_weight", "born_dissolution_time", "born_time", "invincible_time_with_born", "breaking_continue_time", "weekness_duration", "fracture_duration", "behit_light_is_open", "born_effect", "born_client_buffs", "dead_effect", "dead_client_buffs", "hud_in_screen", "blood_mark", "hud_pos_param")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MONSTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    BLOOD_TUBE_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMENT1_FIELD_NUMBER: _ClassVar[int]
    COMMENT2_FIELD_NUMBER: _ClassVar[int]
    SKILL_IDS_FIELD_NUMBER: _ClassVar[int]
    HATRED_BUILD_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_FLYING_FIELD_NUMBER: _ClassVar[int]
    SIGHT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IS_ACCURATE_SIGHT_FIELD_NUMBER: _ClassVar[int]
    HATRED_AWAY_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    HATRED_AWAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_ID_FIELD_NUMBER: _ClassVar[int]
    WALK_SPEED_FIELD_NUMBER: _ClassVar[int]
    RUN_SPEED_FIELD_NUMBER: _ClassVar[int]
    F_RUN_SPEED_FIELD_NUMBER: _ClassVar[int]
    ALERT_SPEED_FIELD_NUMBER: _ClassVar[int]
    MIN_ALERT_DIS_FIELD_NUMBER: _ClassVar[int]
    MAX_ALERT_DIS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_VOXEL_FIELD_NUMBER: _ClassVar[int]
    VOXEL_PATH_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CAMP_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_HP_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TURN_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    AI_TABLE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    ATTACK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DROP_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DASH_SPEED_FIELD_NUMBER: _ClassVar[int]
    MONSTER_FIGHT_AREA_FIELD_NUMBER: _ClassVar[int]
    HATRED_AWAY_SHOW_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TARGET_SELECT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    BORN_DISSOLUTION_TIME_FIELD_NUMBER: _ClassVar[int]
    BORN_TIME_FIELD_NUMBER: _ClassVar[int]
    INVINCIBLE_TIME_WITH_BORN_FIELD_NUMBER: _ClassVar[int]
    BREAKING_CONTINUE_TIME_FIELD_NUMBER: _ClassVar[int]
    WEEKNESS_DURATION_FIELD_NUMBER: _ClassVar[int]
    FRACTURE_DURATION_FIELD_NUMBER: _ClassVar[int]
    BEHIT_LIGHT_IS_OPEN_FIELD_NUMBER: _ClassVar[int]
    BORN_EFFECT_FIELD_NUMBER: _ClassVar[int]
    BORN_CLIENT_BUFFS_FIELD_NUMBER: _ClassVar[int]
    DEAD_EFFECT_FIELD_NUMBER: _ClassVar[int]
    DEAD_CLIENT_BUFFS_FIELD_NUMBER: _ClassVar[int]
    HUD_IN_SCREEN_FIELD_NUMBER: _ClassVar[int]
    BLOOD_MARK_FIELD_NUMBER: _ClassVar[int]
    HUD_POS_PARAM_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    model_id: int
    monster_type: int
    blood_tube_count: int
    comment1: str
    comment2: str
    skill_ids: _table_basic_pb2.int_array
    hatred_build_type: _table_basic_pb2.int_array
    is_flying: bool
    sight_config: _table_basic_pb2.int_table
    is_accurate_sight: bool
    hatred_away: _table_basic_pb2.int_array
    score: int
    hatred_away_type: _table_basic_pb2.int_array
    attribute_id: int
    walk_speed: float
    run_speed: float
    f_run_speed: float
    alert_speed: float
    min_alert_dis: float
    max_alert_dis: float
    export_voxel: bool
    voxel_path: str
    default_camp: int
    is_show_hp: bool
    entity_turn_velocity: _table_basic_pb2.number_array
    ai_table_reference: int
    attack_height: float
    drop_height: float
    dash_speed: float
    monster_fight_area: int
    hatred_away_show: _table_basic_pb2.int_array
    tags: _table_basic_pb2.int_array
    target_select_weight: float
    born_dissolution_time: int
    born_time: int
    invincible_time_with_born: int
    breaking_continue_time: float
    weekness_duration: float
    fracture_duration: float
    behit_light_is_open: bool
    born_effect: str
    born_client_buffs: _table_basic_pb2.int_array
    dead_effect: str
    dead_client_buffs: _table_basic_pb2.int_array
    hud_in_screen: bool
    blood_mark: _table_basic_pb2.int_array
    hud_pos_param: float
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., model_id: _Optional[int] = ..., monster_type: _Optional[int] = ..., blood_tube_count: _Optional[int] = ..., comment1: _Optional[str] = ..., comment2: _Optional[str] = ..., skill_ids: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., hatred_build_type: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., is_flying: bool = ..., sight_config: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., is_accurate_sight: bool = ..., hatred_away: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., score: _Optional[int] = ..., hatred_away_type: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., attribute_id: _Optional[int] = ..., walk_speed: _Optional[float] = ..., run_speed: _Optional[float] = ..., f_run_speed: _Optional[float] = ..., alert_speed: _Optional[float] = ..., min_alert_dis: _Optional[float] = ..., max_alert_dis: _Optional[float] = ..., export_voxel: bool = ..., voxel_path: _Optional[str] = ..., default_camp: _Optional[int] = ..., is_show_hp: bool = ..., entity_turn_velocity: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., ai_table_reference: _Optional[int] = ..., attack_height: _Optional[float] = ..., drop_height: _Optional[float] = ..., dash_speed: _Optional[float] = ..., monster_fight_area: _Optional[int] = ..., hatred_away_show: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., tags: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., target_select_weight: _Optional[float] = ..., born_dissolution_time: _Optional[int] = ..., born_time: _Optional[int] = ..., invincible_time_with_born: _Optional[int] = ..., breaking_continue_time: _Optional[float] = ..., weekness_duration: _Optional[float] = ..., fracture_duration: _Optional[float] = ..., behit_light_is_open: bool = ..., born_effect: _Optional[str] = ..., born_client_buffs: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., dead_effect: _Optional[str] = ..., dead_client_buffs: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., hud_in_screen: bool = ..., blood_mark: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., hud_pos_param: _Optional[float] = ...) -> None: ...

class MonsterTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MonsterTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MonsterTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MonsterTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MonsterTableBase]] = ...) -> None: ...
