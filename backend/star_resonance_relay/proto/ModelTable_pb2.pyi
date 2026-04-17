import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModelTableBase(_message.Message):
    __slots__ = ("model_id", "model_desc", "model_type", "image", "bust", "model_prefab_id", "model_scale", "mount", "mount_offset", "mount_rot", "mount_scale", "weapon_idle_anim", "go_type", "go_data", "body_parts", "rt_pos", "rt_rot", "weight_factor", "stiff_air_curve", "stiff_down_curve", "stiff_fall_curve", "stiff_time", "stiff_stand_time", "stiff_down_time", "death_action_time", "break_end_anim_time", "audio_bank", "ignore_far_cull", "size_type", "basic_fleshy_type", "walk_velocity", "run_velocity", "dash_velocity", "move_anim_speed", "model_effect", "is_multipod", "be_hit_offset", "scale_params", "be_hit_addi_anim_name", "state_additive_hit_weight", "blood_hud_offset")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_DESC_FIELD_NUMBER: _ClassVar[int]
    MODEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    BUST_FIELD_NUMBER: _ClassVar[int]
    MODEL_PREFAB_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_SCALE_FIELD_NUMBER: _ClassVar[int]
    MOUNT_FIELD_NUMBER: _ClassVar[int]
    MOUNT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    MOUNT_ROT_FIELD_NUMBER: _ClassVar[int]
    MOUNT_SCALE_FIELD_NUMBER: _ClassVar[int]
    WEAPON_IDLE_ANIM_FIELD_NUMBER: _ClassVar[int]
    GO_TYPE_FIELD_NUMBER: _ClassVar[int]
    GO_DATA_FIELD_NUMBER: _ClassVar[int]
    BODY_PARTS_FIELD_NUMBER: _ClassVar[int]
    RT_POS_FIELD_NUMBER: _ClassVar[int]
    RT_ROT_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FACTOR_FIELD_NUMBER: _ClassVar[int]
    STIFF_AIR_CURVE_FIELD_NUMBER: _ClassVar[int]
    STIFF_DOWN_CURVE_FIELD_NUMBER: _ClassVar[int]
    STIFF_FALL_CURVE_FIELD_NUMBER: _ClassVar[int]
    STIFF_TIME_FIELD_NUMBER: _ClassVar[int]
    STIFF_STAND_TIME_FIELD_NUMBER: _ClassVar[int]
    STIFF_DOWN_TIME_FIELD_NUMBER: _ClassVar[int]
    DEATH_ACTION_TIME_FIELD_NUMBER: _ClassVar[int]
    BREAK_END_ANIM_TIME_FIELD_NUMBER: _ClassVar[int]
    AUDIO_BANK_FIELD_NUMBER: _ClassVar[int]
    IGNORE_FAR_CULL_FIELD_NUMBER: _ClassVar[int]
    SIZE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BASIC_FLESHY_TYPE_FIELD_NUMBER: _ClassVar[int]
    WALK_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    RUN_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    DASH_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    MOVE_ANIM_SPEED_FIELD_NUMBER: _ClassVar[int]
    MODEL_EFFECT_FIELD_NUMBER: _ClassVar[int]
    IS_MULTIPOD_FIELD_NUMBER: _ClassVar[int]
    BE_HIT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    SCALE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    BE_HIT_ADDI_ANIM_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_ADDITIVE_HIT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    BLOOD_HUD_OFFSET_FIELD_NUMBER: _ClassVar[int]
    model_id: int
    model_desc: str
    model_type: int
    image: str
    bust: str
    model_prefab_id: int
    model_scale: float
    mount: _table_basic_pb2.string_array
    mount_offset: _table_basic_pb2.number_table
    mount_rot: _table_basic_pb2.number_table
    mount_scale: _table_basic_pb2.number_table
    weapon_idle_anim: str
    go_type: int
    go_data: _table_basic_pb2.number_array
    body_parts: _table_basic_pb2.int_array
    rt_pos: _table_basic_pb2.vector3
    rt_rot: _table_basic_pb2.vector3
    weight_factor: float
    stiff_air_curve: _table_basic_pb2.string_array
    stiff_down_curve: _table_basic_pb2.string_array
    stiff_fall_curve: _table_basic_pb2.string_array
    stiff_time: _table_basic_pb2.number_array
    stiff_stand_time: float
    stiff_down_time: float
    death_action_time: int
    break_end_anim_time: float
    audio_bank: _table_basic_pb2.string_array
    ignore_far_cull: bool
    size_type: int
    basic_fleshy_type: int
    walk_velocity: float
    run_velocity: float
    dash_velocity: float
    move_anim_speed: float
    model_effect: str
    is_multipod: bool
    be_hit_offset: float
    scale_params: _table_basic_pb2.number_array
    be_hit_addi_anim_name: str
    state_additive_hit_weight: _table_basic_pb2.number_table
    blood_hud_offset: float
    def __init__(self, model_id: _Optional[int] = ..., model_desc: _Optional[str] = ..., model_type: _Optional[int] = ..., image: _Optional[str] = ..., bust: _Optional[str] = ..., model_prefab_id: _Optional[int] = ..., model_scale: _Optional[float] = ..., mount: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., mount_offset: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., mount_rot: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., mount_scale: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., weapon_idle_anim: _Optional[str] = ..., go_type: _Optional[int] = ..., go_data: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., body_parts: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., rt_pos: _Optional[_Union[_table_basic_pb2.vector3, _Mapping]] = ..., rt_rot: _Optional[_Union[_table_basic_pb2.vector3, _Mapping]] = ..., weight_factor: _Optional[float] = ..., stiff_air_curve: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., stiff_down_curve: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., stiff_fall_curve: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., stiff_time: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., stiff_stand_time: _Optional[float] = ..., stiff_down_time: _Optional[float] = ..., death_action_time: _Optional[int] = ..., break_end_anim_time: _Optional[float] = ..., audio_bank: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., ignore_far_cull: bool = ..., size_type: _Optional[int] = ..., basic_fleshy_type: _Optional[int] = ..., walk_velocity: _Optional[float] = ..., run_velocity: _Optional[float] = ..., dash_velocity: _Optional[float] = ..., move_anim_speed: _Optional[float] = ..., model_effect: _Optional[str] = ..., is_multipod: bool = ..., be_hit_offset: _Optional[float] = ..., scale_params: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., be_hit_addi_anim_name: _Optional[str] = ..., state_additive_hit_weight: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., blood_hud_offset: _Optional[float] = ...) -> None: ...

class ModelTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ModelTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ModelTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ModelTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ModelTableBase]] = ...) -> None: ...
