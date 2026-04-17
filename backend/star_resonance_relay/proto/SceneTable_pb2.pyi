import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneTableBase(_message.Message):
    __slots__ = ("id", "name", "comment", "scene_type", "scene_sub_type", "parent_id", "is_share_parent_scene_data", "scene_resource_id", "loading_png", "scene_ui", "map_size", "map_texs", "map_row_count", "map_tex_size", "big_world", "audio_bank", "scene_enter_type", "born_pos", "born_id", "can_revive", "revive_type", "revive_id", "revive_table_id", "cam_config", "bgm", "loading_bgm", "battle_bgm", "environment_sound", "cam_position", "lua_script", "fall_dis", "weather", "day_and_night", "cutscene_id", "main_ui", "can_change_layer", "max_layer", "preload_cutscenes", "preload_ep_flows", "ep_flow_id", "show_mini_map", "mini_map_ratio", "sub_scene")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    SCENE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCENE_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SHARE_PARENT_SCENE_DATA_FIELD_NUMBER: _ClassVar[int]
    SCENE_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    LOADING_PNG_FIELD_NUMBER: _ClassVar[int]
    SCENE_UI_FIELD_NUMBER: _ClassVar[int]
    MAP_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAP_TEXS_FIELD_NUMBER: _ClassVar[int]
    MAP_ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAP_TEX_SIZE_FIELD_NUMBER: _ClassVar[int]
    BIG_WORLD_FIELD_NUMBER: _ClassVar[int]
    AUDIO_BANK_FIELD_NUMBER: _ClassVar[int]
    SCENE_ENTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    BORN_POS_FIELD_NUMBER: _ClassVar[int]
    BORN_ID_FIELD_NUMBER: _ClassVar[int]
    CAN_REVIVE_FIELD_NUMBER: _ClassVar[int]
    REVIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    REVIVE_ID_FIELD_NUMBER: _ClassVar[int]
    REVIVE_TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    CAM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BGM_FIELD_NUMBER: _ClassVar[int]
    LOADING_BGM_FIELD_NUMBER: _ClassVar[int]
    BATTLE_BGM_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_SOUND_FIELD_NUMBER: _ClassVar[int]
    CAM_POSITION_FIELD_NUMBER: _ClassVar[int]
    LUA_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    FALL_DIS_FIELD_NUMBER: _ClassVar[int]
    WEATHER_FIELD_NUMBER: _ClassVar[int]
    DAY_AND_NIGHT_FIELD_NUMBER: _ClassVar[int]
    CUTSCENE_ID_FIELD_NUMBER: _ClassVar[int]
    MAIN_UI_FIELD_NUMBER: _ClassVar[int]
    CAN_CHANGE_LAYER_FIELD_NUMBER: _ClassVar[int]
    MAX_LAYER_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_CUTSCENES_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_EP_FLOWS_FIELD_NUMBER: _ClassVar[int]
    EP_FLOW_ID_FIELD_NUMBER: _ClassVar[int]
    SHOW_MINI_MAP_FIELD_NUMBER: _ClassVar[int]
    MINI_MAP_RATIO_FIELD_NUMBER: _ClassVar[int]
    SUB_SCENE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    comment: str
    scene_type: int
    scene_sub_type: int
    parent_id: int
    is_share_parent_scene_data: bool
    scene_resource_id: int
    loading_png: str
    scene_ui: _table_basic_pb2.string_array
    map_size: _table_basic_pb2.vector2
    map_texs: _table_basic_pb2.string_array
    map_row_count: int
    map_tex_size: _table_basic_pb2.vector2_array
    big_world: bool
    audio_bank: _table_basic_pb2.string_array
    scene_enter_type: int
    born_pos: _table_basic_pb2.vector3_array
    born_id: int
    can_revive: bool
    revive_type: int
    revive_id: int
    revive_table_id: _table_basic_pb2.int_array
    cam_config: int
    bgm: str
    loading_bgm: str
    battle_bgm: str
    environment_sound: str
    cam_position: _table_basic_pb2.number_array
    lua_script: bool
    fall_dis: float
    weather: int
    day_and_night: int
    cutscene_id: int
    main_ui: int
    can_change_layer: bool
    max_layer: _table_basic_pb2.number_table
    preload_cutscenes: _table_basic_pb2.int_array
    preload_ep_flows: _table_basic_pb2.int_array
    ep_flow_id: int
    show_mini_map: int
    mini_map_ratio: int
    sub_scene: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., comment: _Optional[str] = ..., scene_type: _Optional[int] = ..., scene_sub_type: _Optional[int] = ..., parent_id: _Optional[int] = ..., is_share_parent_scene_data: bool = ..., scene_resource_id: _Optional[int] = ..., loading_png: _Optional[str] = ..., scene_ui: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., map_size: _Optional[_Union[_table_basic_pb2.vector2, _Mapping]] = ..., map_texs: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., map_row_count: _Optional[int] = ..., map_tex_size: _Optional[_Union[_table_basic_pb2.vector2_array, _Mapping]] = ..., big_world: bool = ..., audio_bank: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., scene_enter_type: _Optional[int] = ..., born_pos: _Optional[_Union[_table_basic_pb2.vector3_array, _Mapping]] = ..., born_id: _Optional[int] = ..., can_revive: bool = ..., revive_type: _Optional[int] = ..., revive_id: _Optional[int] = ..., revive_table_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., cam_config: _Optional[int] = ..., bgm: _Optional[str] = ..., loading_bgm: _Optional[str] = ..., battle_bgm: _Optional[str] = ..., environment_sound: _Optional[str] = ..., cam_position: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., lua_script: bool = ..., fall_dis: _Optional[float] = ..., weather: _Optional[int] = ..., day_and_night: _Optional[int] = ..., cutscene_id: _Optional[int] = ..., main_ui: _Optional[int] = ..., can_change_layer: bool = ..., max_layer: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., preload_cutscenes: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., preload_ep_flows: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., ep_flow_id: _Optional[int] = ..., show_mini_map: _Optional[int] = ..., mini_map_ratio: _Optional[int] = ..., sub_scene: _Optional[str] = ...) -> None: ...

class SceneTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SceneTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SceneTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SceneTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SceneTableBase]] = ...) -> None: ...
