import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CollectionTableBase(_message.Message):
    __slots__ = ("id", "collection_name", "show_hud_name", "remark", "type", "model_id", "map_icon", "is_high_light", "visible_condition", "drop_model", "entity_attribute_id", "interact_condition", "pick_range", "pick_action_id", "pick_sound", "pick_time", "buff_in_pick_time", "buff_after_pick", "is_refresh", "ai_config_path", "run_away_ai", "alert_range", "run_away_time", "die_action", "feedback_action", "interaction_template", "interaction_event", "status_info", "status_transition", "default_state", "show_status_info", "show_status_transition")
    ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    SHOW_HUD_NAME_FIELD_NUMBER: _ClassVar[int]
    REMARK_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MAP_ICON_FIELD_NUMBER: _ClassVar[int]
    IS_HIGH_LIGHT_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_CONDITION_FIELD_NUMBER: _ClassVar[int]
    DROP_MODEL_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ATTRIBUTE_ID_FIELD_NUMBER: _ClassVar[int]
    INTERACT_CONDITION_FIELD_NUMBER: _ClassVar[int]
    PICK_RANGE_FIELD_NUMBER: _ClassVar[int]
    PICK_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    PICK_SOUND_FIELD_NUMBER: _ClassVar[int]
    PICK_TIME_FIELD_NUMBER: _ClassVar[int]
    BUFF_IN_PICK_TIME_FIELD_NUMBER: _ClassVar[int]
    BUFF_AFTER_PICK_FIELD_NUMBER: _ClassVar[int]
    IS_REFRESH_FIELD_NUMBER: _ClassVar[int]
    AI_CONFIG_PATH_FIELD_NUMBER: _ClassVar[int]
    RUN_AWAY_AI_FIELD_NUMBER: _ClassVar[int]
    ALERT_RANGE_FIELD_NUMBER: _ClassVar[int]
    RUN_AWAY_TIME_FIELD_NUMBER: _ClassVar[int]
    DIE_ACTION_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_ACTION_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STATE_FIELD_NUMBER: _ClassVar[int]
    SHOW_STATUS_INFO_FIELD_NUMBER: _ClassVar[int]
    SHOW_STATUS_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    id: int
    collection_name: _table_basic_pb2.mlstring
    show_hud_name: bool
    remark: str
    type: int
    model_id: int
    map_icon: int
    is_high_light: bool
    visible_condition: _table_basic_pb2.int_table
    drop_model: int
    entity_attribute_id: int
    interact_condition: _table_basic_pb2.int_array
    pick_range: int
    pick_action_id: int
    pick_sound: str
    pick_time: int
    buff_in_pick_time: int
    buff_after_pick: int
    is_refresh: bool
    ai_config_path: str
    run_away_ai: str
    alert_range: float
    run_away_time: int
    die_action: str
    feedback_action: str
    interaction_template: _table_basic_pb2.int_table
    interaction_event: _table_basic_pb2.string_array
    status_info: _table_basic_pb2.int_table
    status_transition: _table_basic_pb2.int_table
    default_state: int
    show_status_info: _table_basic_pb2.int_table
    show_status_transition: _table_basic_pb2.int_table
    def __init__(self, id: _Optional[int] = ..., collection_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., show_hud_name: bool = ..., remark: _Optional[str] = ..., type: _Optional[int] = ..., model_id: _Optional[int] = ..., map_icon: _Optional[int] = ..., is_high_light: bool = ..., visible_condition: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., drop_model: _Optional[int] = ..., entity_attribute_id: _Optional[int] = ..., interact_condition: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., pick_range: _Optional[int] = ..., pick_action_id: _Optional[int] = ..., pick_sound: _Optional[str] = ..., pick_time: _Optional[int] = ..., buff_in_pick_time: _Optional[int] = ..., buff_after_pick: _Optional[int] = ..., is_refresh: bool = ..., ai_config_path: _Optional[str] = ..., run_away_ai: _Optional[str] = ..., alert_range: _Optional[float] = ..., run_away_time: _Optional[int] = ..., die_action: _Optional[str] = ..., feedback_action: _Optional[str] = ..., interaction_template: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., interaction_event: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., status_info: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., status_transition: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., default_state: _Optional[int] = ..., show_status_info: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., show_status_transition: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class CollectionTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CollectionTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CollectionTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, CollectionTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, CollectionTableBase]] = ...) -> None: ...
