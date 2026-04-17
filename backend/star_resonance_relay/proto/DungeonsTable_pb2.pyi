import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonsTableBase(_message.Message):
    __slots__ = ("id", "name", "content", "function_id", "play_type", "scene_id", "condition", "limited_num", "item_consume", "dungeons_limit", "kick_time", "end_time", "monster_gs", "show_result_hud_type", "result_curscene_pos", "explore_config", "explore_award", "hide_quest", "dungeon_target", "first_pass_award", "pass_award", "count_limit", "fail_text", "disable_transport", "active_state_time", "ready_state_time", "playing_state_time", "settlement_state_time", "exit_transfer_type", "affix", "affix_pool", "attr_grow_range_buff", "dungeons_attr_grow_range")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    PLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    LIMITED_NUM_FIELD_NUMBER: _ClassVar[int]
    ITEM_CONSUME_FIELD_NUMBER: _ClassVar[int]
    DUNGEONS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    KICK_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    MONSTER_GS_FIELD_NUMBER: _ClassVar[int]
    SHOW_RESULT_HUD_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESULT_CURSCENE_POS_FIELD_NUMBER: _ClassVar[int]
    EXPLORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXPLORE_AWARD_FIELD_NUMBER: _ClassVar[int]
    HIDE_QUEST_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_TARGET_FIELD_NUMBER: _ClassVar[int]
    FIRST_PASS_AWARD_FIELD_NUMBER: _ClassVar[int]
    PASS_AWARD_FIELD_NUMBER: _ClassVar[int]
    COUNT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    FAIL_TEXT_FIELD_NUMBER: _ClassVar[int]
    DISABLE_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    READY_STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PLAYING_STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SETTLEMENT_STATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXIT_TRANSFER_TYPE_FIELD_NUMBER: _ClassVar[int]
    AFFIX_FIELD_NUMBER: _ClassVar[int]
    AFFIX_POOL_FIELD_NUMBER: _ClassVar[int]
    ATTR_GROW_RANGE_BUFF_FIELD_NUMBER: _ClassVar[int]
    DUNGEONS_ATTR_GROW_RANGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    content: _table_basic_pb2.mlstring
    function_id: int
    play_type: int
    scene_id: int
    condition: _table_basic_pb2.int_table
    limited_num: _table_basic_pb2.int_array
    item_consume: _table_basic_pb2.int_array
    dungeons_limit: _table_basic_pb2.int_array
    kick_time: int
    end_time: int
    monster_gs: int
    show_result_hud_type: int
    result_curscene_pos: _table_basic_pb2.vector3
    explore_config: _table_basic_pb2.int_array
    explore_award: _table_basic_pb2.int_table
    hide_quest: int
    dungeon_target: _table_basic_pb2.int_table
    first_pass_award: _table_basic_pb2.int_array
    pass_award: _table_basic_pb2.int_array
    count_limit: int
    fail_text: _table_basic_pb2.mlstring
    disable_transport: int
    active_state_time: int
    ready_state_time: int
    playing_state_time: int
    settlement_state_time: int
    exit_transfer_type: int
    affix: _table_basic_pb2.int_array
    affix_pool: int
    attr_grow_range_buff: bool
    dungeons_attr_grow_range: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., content: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., function_id: _Optional[int] = ..., play_type: _Optional[int] = ..., scene_id: _Optional[int] = ..., condition: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., limited_num: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., item_consume: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., dungeons_limit: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., kick_time: _Optional[int] = ..., end_time: _Optional[int] = ..., monster_gs: _Optional[int] = ..., show_result_hud_type: _Optional[int] = ..., result_curscene_pos: _Optional[_Union[_table_basic_pb2.vector3, _Mapping]] = ..., explore_config: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., explore_award: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., hide_quest: _Optional[int] = ..., dungeon_target: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., first_pass_award: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., pass_award: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., count_limit: _Optional[int] = ..., fail_text: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., disable_transport: _Optional[int] = ..., active_state_time: _Optional[int] = ..., ready_state_time: _Optional[int] = ..., playing_state_time: _Optional[int] = ..., settlement_state_time: _Optional[int] = ..., exit_transfer_type: _Optional[int] = ..., affix: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., affix_pool: _Optional[int] = ..., attr_grow_range_buff: bool = ..., dungeons_attr_grow_range: _Optional[int] = ...) -> None: ...

class DungeonsTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: DungeonsTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[DungeonsTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, DungeonsTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, DungeonsTableBase]] = ...) -> None: ...
