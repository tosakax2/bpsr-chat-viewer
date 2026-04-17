import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GlobalParkourTableBase(_message.Message):
    __slots__ = ("index", "id", "value")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    index: int
    id: str
    value: _table_basic_pb2.mlstring
    def __init__(self, index: _Optional[int] = ..., id: _Optional[str] = ..., value: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ...) -> None: ...

class GlobalParkourTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: GlobalParkourTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[GlobalParkourTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, GlobalParkourTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, GlobalParkourTableBase]] = ...) -> None: ...
