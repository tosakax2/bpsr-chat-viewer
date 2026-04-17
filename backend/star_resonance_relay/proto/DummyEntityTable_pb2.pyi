import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DummyEntityTableBase(_message.Message):
    __slots__ = ("u_id", "id", "group_id", "position", "rotation", "refresh_mode", "refresh_after_died", "const_point_refresh", "refresh_range_min", "refresh_range_max", "multi_points_refresh", "refresh_points", "refresh_time_min", "refresh_time_max", "camp_id", "visible", "usable", "shape", "zone_param", "data_type", "export_voxel", "voxel_path", "space_layer_index", "option_data", "scale_effect", "ent_mask", "insight_visible", "is_soft_air_wall", "ignore_visual_layer", "life_info", "visual_layer_id", "source_type", "default_state")
    U_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ROTATION_FIELD_NUMBER: _ClassVar[int]
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
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    ZONE_PARAM_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPORT_VOXEL_FIELD_NUMBER: _ClassVar[int]
    VOXEL_PATH_FIELD_NUMBER: _ClassVar[int]
    SPACE_LAYER_INDEX_FIELD_NUMBER: _ClassVar[int]
    OPTION_DATA_FIELD_NUMBER: _ClassVar[int]
    SCALE_EFFECT_FIELD_NUMBER: _ClassVar[int]
    ENT_MASK_FIELD_NUMBER: _ClassVar[int]
    INSIGHT_VISIBLE_FIELD_NUMBER: _ClassVar[int]
    IS_SOFT_AIR_WALL_FIELD_NUMBER: _ClassVar[int]
    IGNORE_VISUAL_LAYER_FIELD_NUMBER: _ClassVar[int]
    LIFE_INFO_FIELD_NUMBER: _ClassVar[int]
    VISUAL_LAYER_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STATE_FIELD_NUMBER: _ClassVar[int]
    u_id: int
    id: int
    group_id: int
    position: _table_basic_pb2.number_array
    rotation: float
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
    shape: int
    zone_param: _table_basic_pb2.number_array
    data_type: int
    export_voxel: bool
    voxel_path: str
    space_layer_index: int
    option_data: str
    scale_effect: bool
    ent_mask: int
    insight_visible: bool
    is_soft_air_wall: bool
    ignore_visual_layer: bool
    life_info: _table_basic_pb2.int_array
    visual_layer_id: int
    source_type: int
    default_state: int
    def __init__(self, u_id: _Optional[int] = ..., id: _Optional[int] = ..., group_id: _Optional[int] = ..., position: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., rotation: _Optional[float] = ..., refresh_mode: _Optional[int] = ..., refresh_after_died: bool = ..., const_point_refresh: bool = ..., refresh_range_min: _Optional[float] = ..., refresh_range_max: _Optional[float] = ..., multi_points_refresh: bool = ..., refresh_points: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., refresh_time_min: _Optional[float] = ..., refresh_time_max: _Optional[float] = ..., camp_id: _Optional[int] = ..., visible: _Optional[int] = ..., usable: _Optional[int] = ..., shape: _Optional[int] = ..., zone_param: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., data_type: _Optional[int] = ..., export_voxel: bool = ..., voxel_path: _Optional[str] = ..., space_layer_index: _Optional[int] = ..., option_data: _Optional[str] = ..., scale_effect: bool = ..., ent_mask: _Optional[int] = ..., insight_visible: bool = ..., is_soft_air_wall: bool = ..., ignore_visual_layer: bool = ..., life_info: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., visual_layer_id: _Optional[int] = ..., source_type: _Optional[int] = ..., default_state: _Optional[int] = ...) -> None: ...

class DummyEntityTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: DummyEntityTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[DummyEntityTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, DummyEntityTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, DummyEntityTableBase]] = ...) -> None: ...
