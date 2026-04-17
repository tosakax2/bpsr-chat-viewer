import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NameCardTableBase(_message.Message):
    __slots__ = ("id", "name", "unlock_des", "image1", "image2", "unlock")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_DES_FIELD_NUMBER: _ClassVar[int]
    IMAGE1_FIELD_NUMBER: _ClassVar[int]
    IMAGE2_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    unlock_des: _table_basic_pb2.mlstring
    image1: str
    image2: str
    unlock: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., unlock_des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., image1: _Optional[str] = ..., image2: _Optional[str] = ..., unlock: _Optional[int] = ...) -> None: ...

class NameCardTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: NameCardTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[NameCardTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, NameCardTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, NameCardTableBase]] = ...) -> None: ...
