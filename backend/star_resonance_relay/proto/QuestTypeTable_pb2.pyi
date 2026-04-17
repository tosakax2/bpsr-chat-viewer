from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuestTypeTableBase(_message.Message):
    __slots__ = ("quest_type_id", "quest_type_name", "quest_type_group_id", "quest_type_ui", "show_quest_ui", "reset_type", "forced_tracking", "auto_tracking", "quest_list_hide", "order")
    QUEST_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    QUEST_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    QUEST_TYPE_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    QUEST_TYPE_UI_FIELD_NUMBER: _ClassVar[int]
    SHOW_QUEST_UI_FIELD_NUMBER: _ClassVar[int]
    RESET_TYPE_FIELD_NUMBER: _ClassVar[int]
    FORCED_TRACKING_FIELD_NUMBER: _ClassVar[int]
    AUTO_TRACKING_FIELD_NUMBER: _ClassVar[int]
    QUEST_LIST_HIDE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    quest_type_id: int
    quest_type_name: str
    quest_type_group_id: int
    quest_type_ui: str
    show_quest_ui: bool
    reset_type: int
    forced_tracking: bool
    auto_tracking: int
    quest_list_hide: bool
    order: int
    def __init__(self, quest_type_id: _Optional[int] = ..., quest_type_name: _Optional[str] = ..., quest_type_group_id: _Optional[int] = ..., quest_type_ui: _Optional[str] = ..., show_quest_ui: bool = ..., reset_type: _Optional[int] = ..., forced_tracking: bool = ..., auto_tracking: _Optional[int] = ..., quest_list_hide: bool = ..., order: _Optional[int] = ...) -> None: ...

class QuestTypeTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: QuestTypeTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[QuestTypeTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, QuestTypeTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, QuestTypeTableBase]] = ...) -> None: ...
