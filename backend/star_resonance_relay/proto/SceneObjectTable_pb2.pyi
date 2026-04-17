import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneObjectTableBase(_message.Message):
    __slots__ = ("id", "name", "model_id", "attribute_id", "export_voxel", "voxel_path", "default_camp", "is_show_hp", "sobj_be_hit", "sobj_born", "sobj_death", "is_climbable", "scene_obj_type", "end_state_id", "born_effect", "dead_effect", "is_use_prefab_layer", "status_info", "status_transition", "default_state", "interaction_template", "interaction_event", "show_status_info", "show_status_transition")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPORT_VOXEL_FIELD_NUMBER: _ClassVar[int]
    VOXEL_PATH_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CAMP_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_HP_FIELD_NUMBER: _ClassVar[int]
    SOBJ_BE_HIT_FIELD_NUMBER: _ClassVar[int]
    SOBJ_BORN_FIELD_NUMBER: _ClassVar[int]
    SOBJ_DEATH_FIELD_NUMBER: _ClassVar[int]
    IS_CLIMBABLE_FIELD_NUMBER: _ClassVar[int]
    SCENE_OBJ_TYPE_FIELD_NUMBER: _ClassVar[int]
    END_STATE_ID_FIELD_NUMBER: _ClassVar[int]
    BORN_EFFECT_FIELD_NUMBER: _ClassVar[int]
    DEAD_EFFECT_FIELD_NUMBER: _ClassVar[int]
    IS_USE_PREFAB_LAYER_FIELD_NUMBER: _ClassVar[int]
    STATUS_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STATE_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_EVENT_FIELD_NUMBER: _ClassVar[int]
    SHOW_STATUS_INFO_FIELD_NUMBER: _ClassVar[int]
    SHOW_STATUS_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    model_id: int
    attribute_id: int
    export_voxel: bool
    voxel_path: str
    default_camp: int
    is_show_hp: bool
    sobj_be_hit: str
    sobj_born: str
    sobj_death: str
    is_climbable: bool
    scene_obj_type: int
    end_state_id: int
    born_effect: str
    dead_effect: str
    is_use_prefab_layer: bool
    status_info: _table_basic_pb2.int_table
    status_transition: _table_basic_pb2.int_table
    default_state: int
    interaction_template: _table_basic_pb2.int_table
    interaction_event: _table_basic_pb2.string_array
    show_status_info: _table_basic_pb2.int_table
    show_status_transition: _table_basic_pb2.int_table
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., model_id: _Optional[int] = ..., attribute_id: _Optional[int] = ..., export_voxel: bool = ..., voxel_path: _Optional[str] = ..., default_camp: _Optional[int] = ..., is_show_hp: bool = ..., sobj_be_hit: _Optional[str] = ..., sobj_born: _Optional[str] = ..., sobj_death: _Optional[str] = ..., is_climbable: bool = ..., scene_obj_type: _Optional[int] = ..., end_state_id: _Optional[int] = ..., born_effect: _Optional[str] = ..., dead_effect: _Optional[str] = ..., is_use_prefab_layer: bool = ..., status_info: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., status_transition: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., default_state: _Optional[int] = ..., interaction_template: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., interaction_event: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., show_status_info: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., show_status_transition: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class SceneObjectTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SceneObjectTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SceneObjectTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SceneObjectTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SceneObjectTableBase]] = ...) -> None: ...
