import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonNodeDataTableBase(_message.Message):
    __slots__ = ("id", "node_id", "node_level", "node_name", "node_icon", "node_effect", "buff_value_key", "buff_par")
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    NODE_NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_ICON_FIELD_NUMBER: _ClassVar[int]
    NODE_EFFECT_FIELD_NUMBER: _ClassVar[int]
    BUFF_VALUE_KEY_FIELD_NUMBER: _ClassVar[int]
    BUFF_PAR_FIELD_NUMBER: _ClassVar[int]
    id: int
    node_id: int
    node_level: int
    node_name: _table_basic_pb2.mlstring
    node_icon: str
    node_effect: _table_basic_pb2.int_table
    buff_value_key: _table_basic_pb2.string_table
    buff_par: _table_basic_pb2.int_table
    def __init__(self, id: _Optional[int] = ..., node_id: _Optional[int] = ..., node_level: _Optional[int] = ..., node_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., node_icon: _Optional[str] = ..., node_effect: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., buff_value_key: _Optional[_Union[_table_basic_pb2.string_table, _Mapping]] = ..., buff_par: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class SeasonNodeDataTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SeasonNodeDataTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SeasonNodeDataTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SeasonNodeDataTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SeasonNodeDataTableBase]] = ...) -> None: ...
