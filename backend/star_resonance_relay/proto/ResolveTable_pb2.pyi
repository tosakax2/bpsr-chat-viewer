import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResolveTableBase(_message.Message):
    __slots__ = ("id", "item_id", "item_name", "get_item", "function_id", "limit")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
    GET_ITEM_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    item_id: int
    item_name: str
    get_item: _table_basic_pb2.int_array
    function_id: int
    limit: int
    def __init__(self, id: _Optional[int] = ..., item_id: _Optional[int] = ..., item_name: _Optional[str] = ..., get_item: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., function_id: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class ResolveTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ResolveTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ResolveTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ResolveTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ResolveTableBase]] = ...) -> None: ...
