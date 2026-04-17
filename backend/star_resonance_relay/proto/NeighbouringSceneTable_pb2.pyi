import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NeighbouringSceneTableBase(_message.Message):
    __slots__ = ("id", "neighbouring_scene", "portal")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEIGHBOURING_SCENE_FIELD_NUMBER: _ClassVar[int]
    PORTAL_FIELD_NUMBER: _ClassVar[int]
    id: int
    neighbouring_scene: _table_basic_pb2.int_array
    portal: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., neighbouring_scene: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., portal: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class NeighbouringSceneTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: NeighbouringSceneTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[NeighbouringSceneTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, NeighbouringSceneTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, NeighbouringSceneTableBase]] = ...) -> None: ...
