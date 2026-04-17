import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FantasyTypeTableBase(_message.Message):
    __slots__ = ("id", "des", "name", "type_tips", "type_show")
    ID_FIELD_NUMBER: _ClassVar[int]
    DES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_TIPS_FIELD_NUMBER: _ClassVar[int]
    TYPE_SHOW_FIELD_NUMBER: _ClassVar[int]
    id: int
    des: str
    name: _table_basic_pb2.mlstring
    type_tips: str
    type_show: str
    def __init__(self, id: _Optional[int] = ..., des: _Optional[str] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., type_tips: _Optional[str] = ..., type_show: _Optional[str] = ...) -> None: ...

class FantasyTypeTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FantasyTypeTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FantasyTypeTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FantasyTypeTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FantasyTypeTableBase]] = ...) -> None: ...
