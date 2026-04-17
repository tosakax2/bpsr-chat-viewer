import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExploreTableBase(_message.Message):
    __slots__ = ("id", "type", "target_id", "exploration", "param")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    EXPLORATION_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    target_id: int
    exploration: int
    param: _table_basic_pb2.mlstring
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ..., target_id: _Optional[int] = ..., exploration: _Optional[int] = ..., param: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ...) -> None: ...

class ExploreTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ExploreTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ExploreTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ExploreTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ExploreTableBase]] = ...) -> None: ...
