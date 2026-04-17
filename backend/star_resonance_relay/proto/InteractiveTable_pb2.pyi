import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InteractiveTableBase(_message.Message):
    __slots__ = ("id", "trigger_mode", "trigger_btn_id", "trigger_type", "trigger_range", "trigger_angle", "trigger_condition", "is_more", "trigger_time", "insightusable", "model_invisible", "condition", "action", "action_param", "sort_id", "tips_group")
    ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_MODE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_BTN_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_RANGE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_ANGLE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_CONDITION_FIELD_NUMBER: _ClassVar[int]
    IS_MORE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TIME_FIELD_NUMBER: _ClassVar[int]
    INSIGHTUSABLE_FIELD_NUMBER: _ClassVar[int]
    MODEL_INVISIBLE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ACTION_PARAM_FIELD_NUMBER: _ClassVar[int]
    SORT_ID_FIELD_NUMBER: _ClassVar[int]
    TIPS_GROUP_FIELD_NUMBER: _ClassVar[int]
    id: int
    trigger_mode: int
    trigger_btn_id: int
    trigger_type: int
    trigger_range: _table_basic_pb2.number_array
    trigger_angle: int
    trigger_condition: _table_basic_pb2.int_table
    is_more: int
    trigger_time: int
    insightusable: int
    model_invisible: int
    condition: _table_basic_pb2.int_table
    action: str
    action_param: _table_basic_pb2.string_array
    sort_id: int
    tips_group: int
    def __init__(self, id: _Optional[int] = ..., trigger_mode: _Optional[int] = ..., trigger_btn_id: _Optional[int] = ..., trigger_type: _Optional[int] = ..., trigger_range: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., trigger_angle: _Optional[int] = ..., trigger_condition: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., is_more: _Optional[int] = ..., trigger_time: _Optional[int] = ..., insightusable: _Optional[int] = ..., model_invisible: _Optional[int] = ..., condition: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., action: _Optional[str] = ..., action_param: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., sort_id: _Optional[int] = ..., tips_group: _Optional[int] = ...) -> None: ...

class InteractiveTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: InteractiveTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[InteractiveTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, InteractiveTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, InteractiveTableBase]] = ...) -> None: ...
