import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerLevelTableBase(_message.Message):
    __slots__ = ("level", "exp", "level_up_attr", "level_award_id", "icon", "explain_text")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    LEVEL_UP_ATTR_FIELD_NUMBER: _ClassVar[int]
    LEVEL_AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    EXPLAIN_TEXT_FIELD_NUMBER: _ClassVar[int]
    level: int
    exp: int
    level_up_attr: _table_basic_pb2.int_table
    level_award_id: int
    icon: str
    explain_text: _table_basic_pb2.mlstring
    def __init__(self, level: _Optional[int] = ..., exp: _Optional[int] = ..., level_up_attr: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., level_award_id: _Optional[int] = ..., icon: _Optional[str] = ..., explain_text: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ...) -> None: ...

class PlayerLevelTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: PlayerLevelTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[PlayerLevelTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, PlayerLevelTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, PlayerLevelTableBase]] = ...) -> None: ...
