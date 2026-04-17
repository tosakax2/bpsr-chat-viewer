import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MedalTableBase(_message.Message):
    __slots__ = ("id", "name", "type", "unlock_des", "image")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_DES_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    type: int
    unlock_des: _table_basic_pb2.mlstring
    image: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., type: _Optional[int] = ..., unlock_des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., image: _Optional[str] = ...) -> None: ...

class MedalTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MedalTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MedalTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MedalTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MedalTableBase]] = ...) -> None: ...
