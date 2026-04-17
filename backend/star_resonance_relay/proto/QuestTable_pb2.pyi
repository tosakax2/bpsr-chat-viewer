import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuestTableBase(_message.Message):
    __slots__ = ("quest_id", "quest_name", "quest_detail", "quest_type", "quest_step", "award_id", "follow_quest", "pre_quest", "pre_quest_logic", "must_pre_quest", "access_limit", "time_limit", "continue_limit", "abort_limit", "step_flow_path")
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    QUEST_NAME_FIELD_NUMBER: _ClassVar[int]
    QUEST_DETAIL_FIELD_NUMBER: _ClassVar[int]
    QUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUEST_STEP_FIELD_NUMBER: _ClassVar[int]
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    FOLLOW_QUEST_FIELD_NUMBER: _ClassVar[int]
    PRE_QUEST_FIELD_NUMBER: _ClassVar[int]
    PRE_QUEST_LOGIC_FIELD_NUMBER: _ClassVar[int]
    MUST_PRE_QUEST_FIELD_NUMBER: _ClassVar[int]
    ACCESS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ABORT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    STEP_FLOW_PATH_FIELD_NUMBER: _ClassVar[int]
    quest_id: int
    quest_name: _table_basic_pb2.mlstring
    quest_detail: _table_basic_pb2.mlstring
    quest_type: int
    quest_step: int
    award_id: int
    follow_quest: int
    pre_quest: _table_basic_pb2.int_array
    pre_quest_logic: str
    must_pre_quest: _table_basic_pb2.int_array
    access_limit: _table_basic_pb2.string_table
    time_limit: _table_basic_pb2.string_array
    continue_limit: _table_basic_pb2.string_table
    abort_limit: _table_basic_pb2.string_table
    step_flow_path: str
    def __init__(self, quest_id: _Optional[int] = ..., quest_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., quest_detail: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., quest_type: _Optional[int] = ..., quest_step: _Optional[int] = ..., award_id: _Optional[int] = ..., follow_quest: _Optional[int] = ..., pre_quest: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., pre_quest_logic: _Optional[str] = ..., must_pre_quest: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., access_limit: _Optional[_Union[_table_basic_pb2.string_table, _Mapping]] = ..., time_limit: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., continue_limit: _Optional[_Union[_table_basic_pb2.string_table, _Mapping]] = ..., abort_limit: _Optional[_Union[_table_basic_pb2.string_table, _Mapping]] = ..., step_flow_path: _Optional[str] = ...) -> None: ...

class QuestTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: QuestTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[QuestTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, QuestTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, QuestTableBase]] = ...) -> None: ...
