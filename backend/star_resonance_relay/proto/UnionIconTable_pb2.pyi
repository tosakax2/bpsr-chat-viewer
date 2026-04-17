from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnionIconTableBase(_message.Message):
    __slots__ = ("id", "type", "show_icon_route", "resource_route", "show_sort", "colour", "limit", "is_hide")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SHOW_ICON_ROUTE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ROUTE_FIELD_NUMBER: _ClassVar[int]
    SHOW_SORT_FIELD_NUMBER: _ClassVar[int]
    COLOUR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    IS_HIDE_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    show_icon_route: str
    resource_route: str
    show_sort: int
    colour: int
    limit: int
    is_hide: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ..., show_icon_route: _Optional[str] = ..., resource_route: _Optional[str] = ..., show_sort: _Optional[int] = ..., colour: _Optional[int] = ..., limit: _Optional[int] = ..., is_hide: _Optional[int] = ...) -> None: ...

class UnionIconTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: UnionIconTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[UnionIconTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, UnionIconTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, UnionIconTableBase]] = ...) -> None: ...
