import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerLevelSkillTableBase(_message.Message):
    __slots__ = ("buff_id", "buff_name", "active_level", "style", "lock_item")
    BUFF_ID_FIELD_NUMBER: _ClassVar[int]
    BUFF_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    LOCK_ITEM_FIELD_NUMBER: _ClassVar[int]
    buff_id: int
    buff_name: str
    active_level: int
    style: int
    lock_item: _table_basic_pb2.int_table
    def __init__(self, buff_id: _Optional[int] = ..., buff_name: _Optional[str] = ..., active_level: _Optional[int] = ..., style: _Optional[int] = ..., lock_item: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class PlayerLevelSkillTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: PlayerLevelSkillTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[PlayerLevelSkillTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, PlayerLevelSkillTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, PlayerLevelSkillTableBase]] = ...) -> None: ...
