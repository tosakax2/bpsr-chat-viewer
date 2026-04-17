import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProfileImageTableBase(_message.Message):
    __slots__ = ("id", "type", "name", "unlock_des", "image", "unlock")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_DES_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    name: _table_basic_pb2.mlstring
    unlock_des: _table_basic_pb2.mlstring
    image: str
    unlock: int
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., unlock_des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., image: _Optional[str] = ..., unlock: _Optional[int] = ...) -> None: ...

class ProfileImageTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ProfileImageTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ProfileImageTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ProfileImageTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ProfileImageTableBase]] = ...) -> None: ...
