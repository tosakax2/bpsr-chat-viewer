import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkillEffectTableBase(_message.Message):
    __slots__ = ("id", "level", "name", "skill_id", "skill_damage_distance", "effect_range", "ai_release_skill_range", "cool_time_on_battle_start", "use_random_cool_time", "random_pve_cool_time", "tags", "buff_tags", "hit_tags", "entity_tags", "skill_attr_des", "max_horizontal_motion_dis", "st_range", "st_angle", "st_sphere_range", "is_in_battle_state", "take_weapon_in_skill", "need_scale_camera", "skill_learn_buffs")
    ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_DAMAGE_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_RANGE_FIELD_NUMBER: _ClassVar[int]
    AI_RELEASE_SKILL_RANGE_FIELD_NUMBER: _ClassVar[int]
    COOL_TIME_ON_BATTLE_START_FIELD_NUMBER: _ClassVar[int]
    USE_RANDOM_COOL_TIME_FIELD_NUMBER: _ClassVar[int]
    RANDOM_PVE_COOL_TIME_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    BUFF_TAGS_FIELD_NUMBER: _ClassVar[int]
    HIT_TAGS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TAGS_FIELD_NUMBER: _ClassVar[int]
    SKILL_ATTR_DES_FIELD_NUMBER: _ClassVar[int]
    MAX_HORIZONTAL_MOTION_DIS_FIELD_NUMBER: _ClassVar[int]
    ST_RANGE_FIELD_NUMBER: _ClassVar[int]
    ST_ANGLE_FIELD_NUMBER: _ClassVar[int]
    ST_SPHERE_RANGE_FIELD_NUMBER: _ClassVar[int]
    IS_IN_BATTLE_STATE_FIELD_NUMBER: _ClassVar[int]
    TAKE_WEAPON_IN_SKILL_FIELD_NUMBER: _ClassVar[int]
    NEED_SCALE_CAMERA_FIELD_NUMBER: _ClassVar[int]
    SKILL_LEARN_BUFFS_FIELD_NUMBER: _ClassVar[int]
    id: int
    level: int
    name: str
    skill_id: int
    skill_damage_distance: float
    effect_range: _table_basic_pb2.number_array
    ai_release_skill_range: _table_basic_pb2.number_array
    cool_time_on_battle_start: _table_basic_pb2.int_array
    use_random_cool_time: int
    random_pve_cool_time: _table_basic_pb2.number_array
    tags: _table_basic_pb2.int_array
    buff_tags: _table_basic_pb2.int_table
    hit_tags: _table_basic_pb2.int_table
    entity_tags: _table_basic_pb2.int_table
    skill_attr_des: _table_basic_pb2.mlstring_table
    max_horizontal_motion_dis: float
    st_range: float
    st_angle: float
    st_sphere_range: float
    is_in_battle_state: bool
    take_weapon_in_skill: bool
    need_scale_camera: bool
    skill_learn_buffs: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., level: _Optional[int] = ..., name: _Optional[str] = ..., skill_id: _Optional[int] = ..., skill_damage_distance: _Optional[float] = ..., effect_range: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., ai_release_skill_range: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., cool_time_on_battle_start: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., use_random_cool_time: _Optional[int] = ..., random_pve_cool_time: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., tags: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., buff_tags: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., hit_tags: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., entity_tags: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., skill_attr_des: _Optional[_Union[_table_basic_pb2.mlstring_table, _Mapping]] = ..., max_horizontal_motion_dis: _Optional[float] = ..., st_range: _Optional[float] = ..., st_angle: _Optional[float] = ..., st_sphere_range: _Optional[float] = ..., is_in_battle_state: bool = ..., take_weapon_in_skill: bool = ..., need_scale_camera: bool = ..., skill_learn_buffs: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class SkillEffectTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SkillEffectTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SkillEffectTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SkillEffectTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SkillEffectTableBase]] = ...) -> None: ...
