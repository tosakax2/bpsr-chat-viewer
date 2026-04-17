import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ItemPackageTableBase(_message.Message):
    __slots__ = ("id", "name", "icon", "capacity", "show", "classify", "consume", "capacity_extra")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    CLASSIFY_FIELD_NUMBER: _ClassVar[int]
    CONSUME_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_EXTRA_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    icon: str
    capacity: int
    show: int
    classify: _table_basic_pb2.mlstring_table
    consume: str
    capacity_extra: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., icon: _Optional[str] = ..., capacity: _Optional[int] = ..., show: _Optional[int] = ..., classify: _Optional[_Union[_table_basic_pb2.mlstring_table, _Mapping]] = ..., consume: _Optional[str] = ..., capacity_extra: _Optional[int] = ...) -> None: ...

class ItemPackageTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ItemPackageTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ItemPackageTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ItemPackageTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ItemPackageTableBase]] = ...) -> None: ...
