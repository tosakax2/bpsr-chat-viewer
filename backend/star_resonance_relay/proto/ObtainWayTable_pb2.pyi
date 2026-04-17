import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObtainWayTableBase(_message.Message):
    __slots__ = ("id", "get_ways")
    ID_FIELD_NUMBER: _ClassVar[int]
    GET_WAYS_FIELD_NUMBER: _ClassVar[int]
    id: int
    get_ways: _table_basic_pb2.int_table
    def __init__(self, id: _Optional[int] = ..., get_ways: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class ObtainWayTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ObtainWayTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ObtainWayTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ObtainWayTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ObtainWayTableBase]] = ...) -> None: ...
