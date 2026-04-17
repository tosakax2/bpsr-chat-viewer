import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MainIconTableBase(_message.Message):
    __slots__ = ("id", "title", "system_place", "sort_id", "atlas", "icon", "path")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_PLACE_FIELD_NUMBER: _ClassVar[int]
    SORT_ID_FIELD_NUMBER: _ClassVar[int]
    ATLAS_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: _table_basic_pb2.mlstring
    system_place: int
    sort_id: int
    atlas: str
    icon: str
    path: str
    def __init__(self, id: _Optional[int] = ..., title: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., system_place: _Optional[int] = ..., sort_id: _Optional[int] = ..., atlas: _Optional[str] = ..., icon: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class MainIconTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MainIconTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MainIconTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MainIconTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MainIconTableBase]] = ...) -> None: ...
