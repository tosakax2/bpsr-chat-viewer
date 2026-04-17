import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnionManageTableBase(_message.Message):
    __slots__ = ("id", "position", "position_num", "union_manage", "show_sort", "union_authority_sit")
    ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    POSITION_NUM_FIELD_NUMBER: _ClassVar[int]
    UNION_MANAGE_FIELD_NUMBER: _ClassVar[int]
    SHOW_SORT_FIELD_NUMBER: _ClassVar[int]
    UNION_AUTHORITY_SIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    position: _table_basic_pb2.mlstring
    position_num: int
    union_manage: _table_basic_pb2.vector3_array
    show_sort: int
    union_authority_sit: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., position: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., position_num: _Optional[int] = ..., union_manage: _Optional[_Union[_table_basic_pb2.vector3_array, _Mapping]] = ..., show_sort: _Optional[int] = ..., union_authority_sit: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class UnionManageTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: UnionManageTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[UnionManageTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, UnionManageTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, UnionManageTableBase]] = ...) -> None: ...
