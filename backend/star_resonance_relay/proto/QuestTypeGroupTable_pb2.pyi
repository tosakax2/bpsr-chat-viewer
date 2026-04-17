import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuestTypeGroupTableBase(_message.Message):
    __slots__ = ("quest_type_group_id", "group_name", "type_group_ui", "type_group_ui_color", "display_order")
    QUEST_TYPE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_GROUP_UI_FIELD_NUMBER: _ClassVar[int]
    TYPE_GROUP_UI_COLOR_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_ORDER_FIELD_NUMBER: _ClassVar[int]
    quest_type_group_id: int
    group_name: _table_basic_pb2.mlstring
    type_group_ui: str
    type_group_ui_color: str
    display_order: int
    def __init__(self, quest_type_group_id: _Optional[int] = ..., group_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., type_group_ui: _Optional[str] = ..., type_group_ui_color: _Optional[str] = ..., display_order: _Optional[int] = ...) -> None: ...

class QuestTypeGroupTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: QuestTypeGroupTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[QuestTypeGroupTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, QuestTypeGroupTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, QuestTypeGroupTableBase]] = ...) -> None: ...
