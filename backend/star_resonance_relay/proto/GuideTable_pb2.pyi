import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GuideTableBase(_message.Message):
    __slots__ = ("id", "priority", "guide_group", "show_condition_type", "show_condition_value", "check_completion", "trigger_condition_type", "trigger_condition_value", "completion_condition_type", "completion_condition_value", "auto_complete_time", "is_show_ui_frame", "text_around", "text_show_direction", "text_middle", "keyboard_id", "ui_view", "is_black", "show_helplibrary_id", "dynamic_ui")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    GUIDE_GROUP_FIELD_NUMBER: _ClassVar[int]
    SHOW_CONDITION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHOW_CONDITION_VALUE_FIELD_NUMBER: _ClassVar[int]
    CHECK_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_CONDITION_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_CONDITION_VALUE_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_CONDITION_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_CONDITION_VALUE_FIELD_NUMBER: _ClassVar[int]
    AUTO_COMPLETE_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_UI_FRAME_FIELD_NUMBER: _ClassVar[int]
    TEXT_AROUND_FIELD_NUMBER: _ClassVar[int]
    TEXT_SHOW_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    TEXT_MIDDLE_FIELD_NUMBER: _ClassVar[int]
    KEYBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    UI_VIEW_FIELD_NUMBER: _ClassVar[int]
    IS_BLACK_FIELD_NUMBER: _ClassVar[int]
    SHOW_HELPLIBRARY_ID_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_UI_FIELD_NUMBER: _ClassVar[int]
    id: int
    priority: int
    guide_group: int
    show_condition_type: _table_basic_pb2.int_array
    show_condition_value: str
    check_completion: bool
    trigger_condition_type: str
    trigger_condition_value: str
    completion_condition_type: str
    completion_condition_value: str
    auto_complete_time: int
    is_show_ui_frame: bool
    text_around: _table_basic_pb2.mlstring
    text_show_direction: _table_basic_pb2.int_array
    text_middle: _table_basic_pb2.mlstring
    keyboard_id: _table_basic_pb2.int_array
    ui_view: str
    is_black: bool
    show_helplibrary_id: int
    dynamic_ui: _table_basic_pb2.string_array
    def __init__(self, id: _Optional[int] = ..., priority: _Optional[int] = ..., guide_group: _Optional[int] = ..., show_condition_type: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., show_condition_value: _Optional[str] = ..., check_completion: bool = ..., trigger_condition_type: _Optional[str] = ..., trigger_condition_value: _Optional[str] = ..., completion_condition_type: _Optional[str] = ..., completion_condition_value: _Optional[str] = ..., auto_complete_time: _Optional[int] = ..., is_show_ui_frame: bool = ..., text_around: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., text_show_direction: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., text_middle: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., keyboard_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., ui_view: _Optional[str] = ..., is_black: bool = ..., show_helplibrary_id: _Optional[int] = ..., dynamic_ui: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ...) -> None: ...

class GuideTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: GuideTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[GuideTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, GuideTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, GuideTableBase]] = ...) -> None: ...
