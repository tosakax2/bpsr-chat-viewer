import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuestStepTableBase(_message.Message):
    __slots__ = ("quest_step_id", "step_param", "lua_jump", "fail_to_step", "complete_to_step", "complete_all_step", "npc_talk_change", "quest_items", "step_tips", "quest_click_jump", "time_limited_step", "step_target_type", "step_target_condition", "step_target_pos", "step_main_title", "step_target_info", "disable_transport", "scene_check", "visual_layer_check", "hide_track_bar")
    QUEST_STEP_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_PARAM_FIELD_NUMBER: _ClassVar[int]
    LUA_JUMP_FIELD_NUMBER: _ClassVar[int]
    FAIL_TO_STEP_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_TO_STEP_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_ALL_STEP_FIELD_NUMBER: _ClassVar[int]
    NPC_TALK_CHANGE_FIELD_NUMBER: _ClassVar[int]
    QUEST_ITEMS_FIELD_NUMBER: _ClassVar[int]
    STEP_TIPS_FIELD_NUMBER: _ClassVar[int]
    QUEST_CLICK_JUMP_FIELD_NUMBER: _ClassVar[int]
    TIME_LIMITED_STEP_FIELD_NUMBER: _ClassVar[int]
    STEP_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    STEP_TARGET_CONDITION_FIELD_NUMBER: _ClassVar[int]
    STEP_TARGET_POS_FIELD_NUMBER: _ClassVar[int]
    STEP_MAIN_TITLE_FIELD_NUMBER: _ClassVar[int]
    STEP_TARGET_INFO_FIELD_NUMBER: _ClassVar[int]
    DISABLE_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    SCENE_CHECK_FIELD_NUMBER: _ClassVar[int]
    VISUAL_LAYER_CHECK_FIELD_NUMBER: _ClassVar[int]
    HIDE_TRACK_BAR_FIELD_NUMBER: _ClassVar[int]
    quest_step_id: int
    step_param: _table_basic_pb2.int_table
    lua_jump: str
    fail_to_step: int
    complete_to_step: int
    complete_all_step: _table_basic_pb2.int_array
    npc_talk_change: _table_basic_pb2.int_table
    quest_items: _table_basic_pb2.int_table
    step_tips: _table_basic_pb2.mlstring
    quest_click_jump: int
    time_limited_step: _table_basic_pb2.int_array
    step_target_type: int
    step_target_condition: _table_basic_pb2.string_table
    step_target_pos: _table_basic_pb2.string_table
    step_main_title: _table_basic_pb2.mlstring
    step_target_info: _table_basic_pb2.mlstring_array
    disable_transport: int
    scene_check: int
    visual_layer_check: int
    hide_track_bar: bool
    def __init__(self, quest_step_id: _Optional[int] = ..., step_param: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., lua_jump: _Optional[str] = ..., fail_to_step: _Optional[int] = ..., complete_to_step: _Optional[int] = ..., complete_all_step: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., npc_talk_change: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., quest_items: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., step_tips: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., quest_click_jump: _Optional[int] = ..., time_limited_step: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., step_target_type: _Optional[int] = ..., step_target_condition: _Optional[_Union[_table_basic_pb2.string_table, _Mapping]] = ..., step_target_pos: _Optional[_Union[_table_basic_pb2.string_table, _Mapping]] = ..., step_main_title: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., step_target_info: _Optional[_Union[_table_basic_pb2.mlstring_array, _Mapping]] = ..., disable_transport: _Optional[int] = ..., scene_check: _Optional[int] = ..., visual_layer_check: _Optional[int] = ..., hide_track_bar: bool = ...) -> None: ...

class QuestStepTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: QuestStepTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[QuestStepTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, QuestStepTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, QuestStepTableBase]] = ...) -> None: ...
