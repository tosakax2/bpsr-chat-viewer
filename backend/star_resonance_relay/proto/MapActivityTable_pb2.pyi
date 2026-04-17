import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MapActivityTableBase(_message.Message):
    __slots__ = ("id", "name", "scene", "icon", "function_id", "red_dot_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCENE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    RED_DOT_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    scene: _table_basic_pb2.int_array
    icon: str
    function_id: int
    red_dot_id: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., scene: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., icon: _Optional[str] = ..., function_id: _Optional[int] = ..., red_dot_id: _Optional[int] = ...) -> None: ...

class MapActivityTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MapActivityTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MapActivityTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MapActivityTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MapActivityTableBase]] = ...) -> None: ...
