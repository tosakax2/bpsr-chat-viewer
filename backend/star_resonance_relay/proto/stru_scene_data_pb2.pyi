import stru_last_scene_data_pb2 as _stru_last_scene_data_pb2
import stru_position_pb2 as _stru_position_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneData(_message.Message):
    __slots__ = ("map_id", "channel_id", "pos", "level_uuid", "level_pos", "level_map_id", "level_revive_id", "record_id", "plane_id", "scene_layer", "can_switch_layer", "before_fall_pos", "scene_guid", "dungeon_guid", "line_id", "visual_layer_config_id", "last_scene_data", "scene_area_id", "level_area_id", "before_fall_scene_area_id", "static_scene_act_ver")
    class RecordIdEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    LEVEL_UUID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_POS_FIELD_NUMBER: _ClassVar[int]
    LEVEL_MAP_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_REVIVE_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_ID_FIELD_NUMBER: _ClassVar[int]
    PLANE_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_LAYER_FIELD_NUMBER: _ClassVar[int]
    CAN_SWITCH_LAYER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FALL_POS_FIELD_NUMBER: _ClassVar[int]
    SCENE_GUID_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_GUID_FIELD_NUMBER: _ClassVar[int]
    LINE_ID_FIELD_NUMBER: _ClassVar[int]
    VISUAL_LAYER_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_SCENE_DATA_FIELD_NUMBER: _ClassVar[int]
    SCENE_AREA_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_AREA_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FALL_SCENE_AREA_ID_FIELD_NUMBER: _ClassVar[int]
    STATIC_SCENE_ACT_VER_FIELD_NUMBER: _ClassVar[int]
    map_id: int
    channel_id: int
    pos: _stru_position_pb2.Position
    level_uuid: int
    level_pos: _stru_position_pb2.Position
    level_map_id: int
    level_revive_id: int
    record_id: _containers.ScalarMap[int, int]
    plane_id: int
    scene_layer: int
    can_switch_layer: bool
    before_fall_pos: _stru_position_pb2.Position
    scene_guid: str
    dungeon_guid: str
    line_id: int
    visual_layer_config_id: int
    last_scene_data: _stru_last_scene_data_pb2.LastSceneData
    scene_area_id: int
    level_area_id: int
    before_fall_scene_area_id: int
    static_scene_act_ver: int
    def __init__(self, map_id: _Optional[int] = ..., channel_id: _Optional[int] = ..., pos: _Optional[_Union[_stru_position_pb2.Position, _Mapping]] = ..., level_uuid: _Optional[int] = ..., level_pos: _Optional[_Union[_stru_position_pb2.Position, _Mapping]] = ..., level_map_id: _Optional[int] = ..., level_revive_id: _Optional[int] = ..., record_id: _Optional[_Mapping[int, int]] = ..., plane_id: _Optional[int] = ..., scene_layer: _Optional[int] = ..., can_switch_layer: bool = ..., before_fall_pos: _Optional[_Union[_stru_position_pb2.Position, _Mapping]] = ..., scene_guid: _Optional[str] = ..., dungeon_guid: _Optional[str] = ..., line_id: _Optional[int] = ..., visual_layer_config_id: _Optional[int] = ..., last_scene_data: _Optional[_Union[_stru_last_scene_data_pb2.LastSceneData, _Mapping]] = ..., scene_area_id: _Optional[int] = ..., level_area_id: _Optional[int] = ..., before_fall_scene_area_id: _Optional[int] = ..., static_scene_act_ver: _Optional[int] = ...) -> None: ...
