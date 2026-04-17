import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ItemTypeTableBase(_message.Message):
    __slots__ = ("id", "name", "package", "classify", "sort_id", "preview_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    CLASSIFY_FIELD_NUMBER: _ClassVar[int]
    SORT_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    package: int
    classify: int
    sort_id: int
    preview_id: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., package: _Optional[int] = ..., classify: _Optional[int] = ..., sort_id: _Optional[int] = ..., preview_id: _Optional[int] = ...) -> None: ...

class ItemTypeTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ItemTypeTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ItemTypeTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ItemTypeTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ItemTypeTableBase]] = ...) -> None: ...
