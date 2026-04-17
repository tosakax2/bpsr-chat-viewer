import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonTitleTableBase(_message.Message):
    __slots__ = ("id", "name", "content", "weight")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    content: _table_basic_pb2.mlstring
    weight: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., content: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., weight: _Optional[int] = ...) -> None: ...

class DungeonTitleTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: DungeonTitleTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[DungeonTitleTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, DungeonTitleTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, DungeonTitleTableBase]] = ...) -> None: ...
