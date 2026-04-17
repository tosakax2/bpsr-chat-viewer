import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FunctionTableBase(_message.Message):
    __slots__ = ("id", "name", "note", "atlas", "dialog_icon", "icon", "function_order", "parent_id", "level", "role_level", "quest_id", "quest_step_id", "timer_id", "on_off", "preview", "preview_text", "open_tips")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    ATLAS_FIELD_NUMBER: _ClassVar[int]
    DIALOG_ICON_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ORDER_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    ROLE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    QUEST_ID_FIELD_NUMBER: _ClassVar[int]
    QUEST_STEP_ID_FIELD_NUMBER: _ClassVar[int]
    TIMER_ID_FIELD_NUMBER: _ClassVar[int]
    ON_OFF_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_TEXT_FIELD_NUMBER: _ClassVar[int]
    OPEN_TIPS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    note: str
    atlas: str
    dialog_icon: str
    icon: str
    function_order: _table_basic_pb2.string_array
    parent_id: int
    level: int
    role_level: int
    quest_id: int
    quest_step_id: _table_basic_pb2.int_array
    timer_id: int
    on_off: int
    preview: int
    preview_text: _table_basic_pb2.mlstring
    open_tips: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., note: _Optional[str] = ..., atlas: _Optional[str] = ..., dialog_icon: _Optional[str] = ..., icon: _Optional[str] = ..., function_order: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., parent_id: _Optional[int] = ..., level: _Optional[int] = ..., role_level: _Optional[int] = ..., quest_id: _Optional[int] = ..., quest_step_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., timer_id: _Optional[int] = ..., on_off: _Optional[int] = ..., preview: _Optional[int] = ..., preview_text: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., open_tips: _Optional[int] = ...) -> None: ...

class FunctionTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FunctionTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FunctionTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FunctionTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FunctionTableBase]] = ...) -> None: ...
