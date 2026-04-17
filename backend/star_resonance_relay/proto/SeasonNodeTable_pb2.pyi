import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonNodeTableBase(_message.Message):
    __slots__ = ("id", "hole_id", "hole_level", "node_id", "node_type", "season_id", "node_collection", "collection", "number_consume", "other_consume")
    ID_FIELD_NUMBER: _ClassVar[int]
    HOLE_ID_FIELD_NUMBER: _ClassVar[int]
    HOLE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    NUMBER_CONSUME_FIELD_NUMBER: _ClassVar[int]
    OTHER_CONSUME_FIELD_NUMBER: _ClassVar[int]
    id: int
    hole_id: int
    hole_level: int
    node_id: _table_basic_pb2.int_array
    node_type: int
    season_id: int
    node_collection: _table_basic_pb2.int_table
    collection: _table_basic_pb2.int_table
    number_consume: _table_basic_pb2.int_table
    other_consume: _table_basic_pb2.int_table
    def __init__(self, id: _Optional[int] = ..., hole_id: _Optional[int] = ..., hole_level: _Optional[int] = ..., node_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., node_type: _Optional[int] = ..., season_id: _Optional[int] = ..., node_collection: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., collection: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., number_consume: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., other_consume: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class SeasonNodeTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SeasonNodeTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SeasonNodeTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SeasonNodeTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SeasonNodeTableBase]] = ...) -> None: ...
