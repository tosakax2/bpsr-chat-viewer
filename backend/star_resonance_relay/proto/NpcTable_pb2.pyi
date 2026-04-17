import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NpcTableBase(_message.Message):
    __slots__ = ("id", "name", "model_id", "ai_config_file", "walk_speed", "run_speed", "export_voxel", "voxel_path", "default_camp", "is_show_hp", "entity_turn_velocity", "map_icon", "title", "dialog_flow", "comment", "npc_icon", "show_type", "show_name", "npc_function_id", "scene_tag_id", "is_turn_to_player", "talk_action_id", "look_at_position", "look_at_npc", "look_at_player", "look_at_distance", "look_at_angle", "loot_at_weight", "response_range", "scare_action_id", "praise_action_id", "be_pushed_action_id", "layer", "insightusable", "born_effect", "born_time", "born_client_buffs", "dead_effect", "dead_client_buffs", "use_ik", "is_dissolution", "plot_characters_id", "status_info", "status_transition", "interaction_template", "interaction_event", "default_state", "show_status_info", "show_status_transition")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    AI_CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    WALK_SPEED_FIELD_NUMBER: _ClassVar[int]
    RUN_SPEED_FIELD_NUMBER: _ClassVar[int]
    EXPORT_VOXEL_FIELD_NUMBER: _ClassVar[int]
    VOXEL_PATH_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CAMP_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_HP_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TURN_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    MAP_ICON_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DIALOG_FLOW_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    NPC_ICON_FIELD_NUMBER: _ClassVar[int]
    SHOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHOW_NAME_FIELD_NUMBER: _ClassVar[int]
    NPC_FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_TAG_ID_FIELD_NUMBER: _ClassVar[int]
    IS_TURN_TO_PLAYER_FIELD_NUMBER: _ClassVar[int]
    TALK_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    LOOK_AT_POSITION_FIELD_NUMBER: _ClassVar[int]
    LOOK_AT_NPC_FIELD_NUMBER: _ClassVar[int]
    LOOK_AT_PLAYER_FIELD_NUMBER: _ClassVar[int]
    LOOK_AT_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    LOOK_AT_ANGLE_FIELD_NUMBER: _ClassVar[int]
    LOOT_AT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_RANGE_FIELD_NUMBER: _ClassVar[int]
    SCARE_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    PRAISE_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    BE_PUSHED_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    LAYER_FIELD_NUMBER: _ClassVar[int]
    INSIGHTUSABLE_FIELD_NUMBER: _ClassVar[int]
    BORN_EFFECT_FIELD_NUMBER: _ClassVar[int]
    BORN_TIME_FIELD_NUMBER: _ClassVar[int]
    BORN_CLIENT_BUFFS_FIELD_NUMBER: _ClassVar[int]
    DEAD_EFFECT_FIELD_NUMBER: _ClassVar[int]
    DEAD_CLIENT_BUFFS_FIELD_NUMBER: _ClassVar[int]
    USE_IK_FIELD_NUMBER: _ClassVar[int]
    IS_DISSOLUTION_FIELD_NUMBER: _ClassVar[int]
    PLOT_CHARACTERS_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STATE_FIELD_NUMBER: _ClassVar[int]
    SHOW_STATUS_INFO_FIELD_NUMBER: _ClassVar[int]
    SHOW_STATUS_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    model_id: int
    ai_config_file: str
    walk_speed: float
    run_speed: float
    export_voxel: bool
    voxel_path: str
    default_camp: int
    is_show_hp: bool
    entity_turn_velocity: _table_basic_pb2.number_array
    map_icon: str
    title: _table_basic_pb2.mlstring
    dialog_flow: int
    comment: str
    npc_icon: str
    show_type: bool
    show_name: int
    npc_function_id: _table_basic_pb2.mlstring_table
    scene_tag_id: int
    is_turn_to_player: bool
    talk_action_id: int
    look_at_position: _table_basic_pb2.vector3
    look_at_npc: int
    look_at_player: str
    look_at_distance: int
    look_at_angle: int
    loot_at_weight: _table_basic_pb2.number_array
    response_range: int
    scare_action_id: int
    praise_action_id: int
    be_pushed_action_id: _table_basic_pb2.int_array
    layer: int
    insightusable: int
    born_effect: str
    born_time: int
    born_client_buffs: _table_basic_pb2.int_array
    dead_effect: str
    dead_client_buffs: _table_basic_pb2.int_array
    use_ik: bool
    is_dissolution: bool
    plot_characters_id: int
    status_info: _table_basic_pb2.int_table
    status_transition: _table_basic_pb2.int_table
    interaction_template: _table_basic_pb2.int_table
    interaction_event: _table_basic_pb2.string_array
    default_state: int
    show_status_info: _table_basic_pb2.int_table
    show_status_transition: _table_basic_pb2.int_table
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., model_id: _Optional[int] = ..., ai_config_file: _Optional[str] = ..., walk_speed: _Optional[float] = ..., run_speed: _Optional[float] = ..., export_voxel: bool = ..., voxel_path: _Optional[str] = ..., default_camp: _Optional[int] = ..., is_show_hp: bool = ..., entity_turn_velocity: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., map_icon: _Optional[str] = ..., title: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., dialog_flow: _Optional[int] = ..., comment: _Optional[str] = ..., npc_icon: _Optional[str] = ..., show_type: bool = ..., show_name: _Optional[int] = ..., npc_function_id: _Optional[_Union[_table_basic_pb2.mlstring_table, _Mapping]] = ..., scene_tag_id: _Optional[int] = ..., is_turn_to_player: bool = ..., talk_action_id: _Optional[int] = ..., look_at_position: _Optional[_Union[_table_basic_pb2.vector3, _Mapping]] = ..., look_at_npc: _Optional[int] = ..., look_at_player: _Optional[str] = ..., look_at_distance: _Optional[int] = ..., look_at_angle: _Optional[int] = ..., loot_at_weight: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., response_range: _Optional[int] = ..., scare_action_id: _Optional[int] = ..., praise_action_id: _Optional[int] = ..., be_pushed_action_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., layer: _Optional[int] = ..., insightusable: _Optional[int] = ..., born_effect: _Optional[str] = ..., born_time: _Optional[int] = ..., born_client_buffs: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., dead_effect: _Optional[str] = ..., dead_client_buffs: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., use_ik: bool = ..., is_dissolution: bool = ..., plot_characters_id: _Optional[int] = ..., status_info: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., status_transition: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., interaction_template: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., interaction_event: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., default_state: _Optional[int] = ..., show_status_info: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., show_status_transition: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class NpcTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: NpcTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[NpcTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, NpcTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, NpcTableBase]] = ...) -> None: ...
