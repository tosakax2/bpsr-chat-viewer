import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CampRelationshipTableBase(_message.Message):
    __slots__ = ("map_id", "relationship_id")
    MAP_ID_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_ID_FIELD_NUMBER: _ClassVar[int]
    map_id: int
    relationship_id: _table_basic_pb2.int_table
    def __init__(self, map_id: _Optional[int] = ..., relationship_id: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class CampRelationshipTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: CampRelationshipTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[CampRelationshipTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, CampRelationshipTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, CampRelationshipTableBase]] = ...) -> None: ...
