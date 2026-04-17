import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FantasyHoleTableBase(_message.Message):
    __slots__ = ("id", "des", "hole_icon", "unlock", "unlock_consume", "fantasytype")
    ID_FIELD_NUMBER: _ClassVar[int]
    DES_FIELD_NUMBER: _ClassVar[int]
    HOLE_ICON_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_CONSUME_FIELD_NUMBER: _ClassVar[int]
    FANTASYTYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    des: str
    hole_icon: str
    unlock: _table_basic_pb2.int_table
    unlock_consume: _table_basic_pb2.int_table
    fantasytype: int
    def __init__(self, id: _Optional[int] = ..., des: _Optional[str] = ..., hole_icon: _Optional[str] = ..., unlock: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., unlock_consume: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., fantasytype: _Optional[int] = ...) -> None: ...

class FantasyHoleTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FantasyHoleTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FantasyHoleTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FantasyHoleTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FantasyHoleTableBase]] = ...) -> None: ...
