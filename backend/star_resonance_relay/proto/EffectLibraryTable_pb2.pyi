import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EffectLibraryTableBase(_message.Message):
    __slots__ = ("id", "name", "path", "tags", "thumbnail")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    path: str
    tags: _table_basic_pb2.string_array
    thumbnail: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., path: _Optional[str] = ..., tags: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., thumbnail: _Optional[str] = ...) -> None: ...

class EffectLibraryTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: EffectLibraryTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[EffectLibraryTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, EffectLibraryTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, EffectLibraryTableBase]] = ...) -> None: ...
