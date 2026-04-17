import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneTagTableBase(_message.Message):
    __slots__ = ("id", "name", "icon1", "icon2", "type", "param", "function_id", "track_type", "show", "unlock", "level", "sort", "number", "mini_show", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON1_FIELD_NUMBER: _ClassVar[int]
    ICON2_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    TRACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    MINI_SHOW_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    icon1: str
    icon2: str
    type: int
    param: str
    function_id: int
    track_type: int
    show: int
    unlock: int
    level: int
    sort: int
    number: int
    mini_show: int
    description: _table_basic_pb2.mlstring
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., icon1: _Optional[str] = ..., icon2: _Optional[str] = ..., type: _Optional[int] = ..., param: _Optional[str] = ..., function_id: _Optional[int] = ..., track_type: _Optional[int] = ..., show: _Optional[int] = ..., unlock: _Optional[int] = ..., level: _Optional[int] = ..., sort: _Optional[int] = ..., number: _Optional[int] = ..., mini_show: _Optional[int] = ..., description: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ...) -> None: ...

class SceneTagTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SceneTagTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SceneTagTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SceneTagTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SceneTagTableBase]] = ...) -> None: ...
