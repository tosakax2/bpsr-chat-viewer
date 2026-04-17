import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuffTableBase(_message.Message):
    __slots__ = ("id", "level", "name_design", "note", "name", "icon", "desc", "buff_type", "buff_priority", "tips_description", "visible", "repeat_add_rule", "destroy_param", "delete_dead", "delete_offline", "delete_change_scene", "delete_change_visual_layer", "delete_weapon_change", "tags", "special_attr", "buff_ability_type", "is_client_buff", "show_hud_icon", "hud_switch")
    ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    NAME_DESIGN_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    BUFF_TYPE_FIELD_NUMBER: _ClassVar[int]
    BUFF_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    TIPS_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    REPEAT_ADD_RULE_FIELD_NUMBER: _ClassVar[int]
    DESTROY_PARAM_FIELD_NUMBER: _ClassVar[int]
    DELETE_DEAD_FIELD_NUMBER: _ClassVar[int]
    DELETE_OFFLINE_FIELD_NUMBER: _ClassVar[int]
    DELETE_CHANGE_SCENE_FIELD_NUMBER: _ClassVar[int]
    DELETE_CHANGE_VISUAL_LAYER_FIELD_NUMBER: _ClassVar[int]
    DELETE_WEAPON_CHANGE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_ATTR_FIELD_NUMBER: _ClassVar[int]
    BUFF_ABILITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_CLIENT_BUFF_FIELD_NUMBER: _ClassVar[int]
    SHOW_HUD_ICON_FIELD_NUMBER: _ClassVar[int]
    HUD_SWITCH_FIELD_NUMBER: _ClassVar[int]
    id: int
    level: int
    name_design: str
    note: str
    name: _table_basic_pb2.mlstring
    icon: str
    desc: _table_basic_pb2.mlstring
    buff_type: int
    buff_priority: int
    tips_description: int
    visible: int
    repeat_add_rule: _table_basic_pb2.int_array
    destroy_param: _table_basic_pb2.number_table
    delete_dead: bool
    delete_offline: bool
    delete_change_scene: bool
    delete_change_visual_layer: bool
    delete_weapon_change: bool
    tags: _table_basic_pb2.int_array
    special_attr: _table_basic_pb2.int_array
    buff_ability_type: int
    is_client_buff: bool
    show_hud_icon: str
    hud_switch: int
    def __init__(self, id: _Optional[int] = ..., level: _Optional[int] = ..., name_design: _Optional[str] = ..., note: _Optional[str] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., icon: _Optional[str] = ..., desc: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., buff_type: _Optional[int] = ..., buff_priority: _Optional[int] = ..., tips_description: _Optional[int] = ..., visible: _Optional[int] = ..., repeat_add_rule: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., destroy_param: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., delete_dead: bool = ..., delete_offline: bool = ..., delete_change_scene: bool = ..., delete_change_visual_layer: bool = ..., delete_weapon_change: bool = ..., tags: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., special_attr: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., buff_ability_type: _Optional[int] = ..., is_client_buff: bool = ..., show_hud_icon: _Optional[str] = ..., hud_switch: _Optional[int] = ...) -> None: ...

class BuffTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BuffTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BuffTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, BuffTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, BuffTableBase]] = ...) -> None: ...
