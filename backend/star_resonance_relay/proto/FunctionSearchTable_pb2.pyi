import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FunctionSearchTableBase(_message.Message):
    __slots__ = ("id", "sort", "quick_jump_type", "quick_jump_param", "is_hide")
    ID_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    QUICK_JUMP_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUICK_JUMP_PARAM_FIELD_NUMBER: _ClassVar[int]
    IS_HIDE_FIELD_NUMBER: _ClassVar[int]
    id: int
    sort: int
    quick_jump_type: int
    quick_jump_param: _table_basic_pb2.int_array
    is_hide: int
    def __init__(self, id: _Optional[int] = ..., sort: _Optional[int] = ..., quick_jump_type: _Optional[int] = ..., quick_jump_param: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., is_hide: _Optional[int] = ...) -> None: ...

class FunctionSearchTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FunctionSearchTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FunctionSearchTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FunctionSearchTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FunctionSearchTableBase]] = ...) -> None: ...
