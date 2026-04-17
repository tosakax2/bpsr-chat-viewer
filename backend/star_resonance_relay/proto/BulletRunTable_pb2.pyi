import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BulletRunTableBase(_message.Message):
    __slots__ = ("id", "motion_type", "start_speed", "accelerated_speed", "max_speed", "direction_type", "is_follow_target", "max_follow_angle", "ex_start_speed", "ex_accelerated_speed", "ex_max_speed", "curve_path", "curve_id", "is_random_radian", "random_pos_top", "random_pos_bottom", "random_pos_left", "random_pos_right", "follow_type", "offset_pos", "original_dir", "min_zoom", "max_zoom", "zoom_speed", "zoom_is_loop", "follow_config_id", "check_obstacle", "is_stand", "is_lock_target", "is_can_dodge")
    ID_FIELD_NUMBER: _ClassVar[int]
    MOTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_SPEED_FIELD_NUMBER: _ClassVar[int]
    ACCELERATED_SPEED_FIELD_NUMBER: _ClassVar[int]
    MAX_SPEED_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_FOLLOW_TARGET_FIELD_NUMBER: _ClassVar[int]
    MAX_FOLLOW_ANGLE_FIELD_NUMBER: _ClassVar[int]
    EX_START_SPEED_FIELD_NUMBER: _ClassVar[int]
    EX_ACCELERATED_SPEED_FIELD_NUMBER: _ClassVar[int]
    EX_MAX_SPEED_FIELD_NUMBER: _ClassVar[int]
    CURVE_PATH_FIELD_NUMBER: _ClassVar[int]
    CURVE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_RANDOM_RADIAN_FIELD_NUMBER: _ClassVar[int]
    RANDOM_POS_TOP_FIELD_NUMBER: _ClassVar[int]
    RANDOM_POS_BOTTOM_FIELD_NUMBER: _ClassVar[int]
    RANDOM_POS_LEFT_FIELD_NUMBER: _ClassVar[int]
    RANDOM_POS_RIGHT_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_POS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_DIR_FIELD_NUMBER: _ClassVar[int]
    MIN_ZOOM_FIELD_NUMBER: _ClassVar[int]
    MAX_ZOOM_FIELD_NUMBER: _ClassVar[int]
    ZOOM_SPEED_FIELD_NUMBER: _ClassVar[int]
    ZOOM_IS_LOOP_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    CHECK_OBSTACLE_FIELD_NUMBER: _ClassVar[int]
    IS_STAND_FIELD_NUMBER: _ClassVar[int]
    IS_LOCK_TARGET_FIELD_NUMBER: _ClassVar[int]
    IS_CAN_DODGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    motion_type: int
    start_speed: float
    accelerated_speed: float
    max_speed: float
    direction_type: int
    is_follow_target: bool
    max_follow_angle: float
    ex_start_speed: float
    ex_accelerated_speed: float
    ex_max_speed: float
    curve_path: str
    curve_id: int
    is_random_radian: bool
    random_pos_top: float
    random_pos_bottom: float
    random_pos_left: float
    random_pos_right: float
    follow_type: int
    offset_pos: _table_basic_pb2.vector3
    original_dir: float
    min_zoom: float
    max_zoom: float
    zoom_speed: float
    zoom_is_loop: bool
    follow_config_id: int
    check_obstacle: bool
    is_stand: bool
    is_lock_target: bool
    is_can_dodge: bool
    def __init__(self, id: _Optional[int] = ..., motion_type: _Optional[int] = ..., start_speed: _Optional[float] = ..., accelerated_speed: _Optional[float] = ..., max_speed: _Optional[float] = ..., direction_type: _Optional[int] = ..., is_follow_target: bool = ..., max_follow_angle: _Optional[float] = ..., ex_start_speed: _Optional[float] = ..., ex_accelerated_speed: _Optional[float] = ..., ex_max_speed: _Optional[float] = ..., curve_path: _Optional[str] = ..., curve_id: _Optional[int] = ..., is_random_radian: bool = ..., random_pos_top: _Optional[float] = ..., random_pos_bottom: _Optional[float] = ..., random_pos_left: _Optional[float] = ..., random_pos_right: _Optional[float] = ..., follow_type: _Optional[int] = ..., offset_pos: _Optional[_Union[_table_basic_pb2.vector3, _Mapping]] = ..., original_dir: _Optional[float] = ..., min_zoom: _Optional[float] = ..., max_zoom: _Optional[float] = ..., zoom_speed: _Optional[float] = ..., zoom_is_loop: bool = ..., follow_config_id: _Optional[int] = ..., check_obstacle: bool = ..., is_stand: bool = ..., is_lock_target: bool = ..., is_can_dodge: bool = ...) -> None: ...

class BulletRunTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BulletRunTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BulletRunTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, BulletRunTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, BulletRunTableBase]] = ...) -> None: ...
