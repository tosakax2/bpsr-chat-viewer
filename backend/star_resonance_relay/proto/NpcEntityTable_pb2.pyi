import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NpcEntityTableBase(_message.Message):
    __slots__ = ("u_id", "id", "group_id", "position", "rotation", "rotationx", "rotationz", "refresh_mode", "refresh_after_died", "const_point_refresh", "refresh_range_min", "refresh_range_max", "multi_points_refresh", "refresh_points", "refresh_time_min", "refresh_time_max", "camp_id", "visible", "usable", "data_type", "space_layer_index", "override_scale", "ent_mask", "alert_range", "refresh_condition", "client_ai_config_file", "ignore_visual_layer", "bind_task_id", "is_not_ground", "is_static", "is_ai_enabled", "visual_layer_id", "default_idl_anim", "source_type", "default_state", "interaction_template", "interaction_event")
    U_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ROTATION_FIELD_NUMBER: _ClassVar[int]
    ROTATIONX_FIELD_NUMBER: _ClassVar[int]
    ROTATIONZ_FIELD_NUMBER: _ClassVar[int]
    REFRESH_MODE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_AFTER_DIED_FIELD_NUMBER: _ClassVar[int]
    CONST_POINT_REFRESH_FIELD_NUMBER: _ClassVar[int]
    REFRESH_RANGE_MIN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_RANGE_MAX_FIELD_NUMBER: _ClassVar[int]
    MULTI_POINTS_REFRESH_FIELD_NUMBER: _ClassVar[int]
    REFRESH_POINTS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TIME_MIN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TIME_MAX_FIELD_NUMBER: _ClassVar[int]
    CAMP_ID_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    USABLE_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPACE_LAYER_INDEX_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_SCALE_FIELD_NUMBER: _ClassVar[int]
    ENT_MASK_FIELD_NUMBER: _ClassVar[int]
    ALERT_RANGE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_CONDITION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_AI_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_VISUAL_LAYER_FIELD_NUMBER: _ClassVar[int]
    BIND_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_GROUND_FIELD_NUMBER: _ClassVar[int]
    IS_STATIC_FIELD_NUMBER: _ClassVar[int]
    IS_AI_ENABLED_FIELD_NUMBER: _ClassVar[int]
    VISUAL_LAYER_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_IDL_ANIM_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STATE_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    u_id: int
    id: int
    group_id: int
    position: _table_basic_pb2.number_array
    rotation: float
    rotationx: float
    rotationz: float
    refresh_mode: int
    refresh_after_died: bool
    const_point_refresh: bool
    refresh_range_min: float
    refresh_range_max: float
    multi_points_refresh: bool
    refresh_points: _table_basic_pb2.number_array
    refresh_time_min: float
    refresh_time_max: float
    camp_id: int
    visible: int
    usable: int
    data_type: int
    space_layer_index: int
    override_scale: float
    ent_mask: int
    alert_range: float
    refresh_condition: _table_basic_pb2.int_table
    client_ai_config_file: str
    ignore_visual_layer: bool
    bind_task_id: int
    is_not_ground: bool
    is_static: bool
    is_ai_enabled: bool
    visual_layer_id: int
    default_idl_anim: str
    source_type: int
    default_state: int
    interaction_template: _table_basic_pb2.int_table
    interaction_event: _table_basic_pb2.string_array
    def __init__(self, u_id: _Optional[int] = ..., id: _Optional[int] = ..., group_id: _Optional[int] = ..., position: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., rotation: _Optional[float] = ..., rotationx: _Optional[float] = ..., rotationz: _Optional[float] = ..., refresh_mode: _Optional[int] = ..., refresh_after_died: bool = ..., const_point_refresh: bool = ..., refresh_range_min: _Optional[float] = ..., refresh_range_max: _Optional[float] = ..., multi_points_refresh: bool = ..., refresh_points: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., refresh_time_min: _Optional[float] = ..., refresh_time_max: _Optional[float] = ..., camp_id: _Optional[int] = ..., visible: _Optional[int] = ..., usable: _Optional[int] = ..., data_type: _Optional[int] = ..., space_layer_index: _Optional[int] = ..., override_scale: _Optional[float] = ..., ent_mask: _Optional[int] = ..., alert_range: _Optional[float] = ..., refresh_condition: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., client_ai_config_file: _Optional[str] = ..., ignore_visual_layer: bool = ..., bind_task_id: _Optional[int] = ..., is_not_ground: bool = ..., is_static: bool = ..., is_ai_enabled: bool = ..., visual_layer_id: _Optional[int] = ..., default_idl_anim: _Optional[str] = ..., source_type: _Optional[int] = ..., default_state: _Optional[int] = ..., interaction_template: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., interaction_event: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ...) -> None: ...

class NpcEntityTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: NpcEntityTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[NpcEntityTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, NpcEntityTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, NpcEntityTableBase]] = ...) -> None: ...
