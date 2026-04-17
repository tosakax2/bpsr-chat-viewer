import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoleCardTableBase(_message.Message):
    __slots__ = ("id", "function_id", "name", "system", "show", "sort", "check", "icon")
    ID_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CHECK_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    id: int
    function_id: str
    name: _table_basic_pb2.mlstring
    system: str
    show: str
    sort: str
    check: str
    icon: str
    def __init__(self, id: _Optional[int] = ..., function_id: _Optional[str] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., system: _Optional[str] = ..., show: _Optional[str] = ..., sort: _Optional[str] = ..., check: _Optional[str] = ..., icon: _Optional[str] = ...) -> None: ...

class RoleCardTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: RoleCardTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[RoleCardTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, RoleCardTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, RoleCardTableBase]] = ...) -> None: ...
