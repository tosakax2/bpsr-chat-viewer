import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FantasySolutionTableBase(_message.Message):
    __slots__ = ("id", "name", "des", "recommended_type", "recommend_fantasy_list")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DES_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_TYPE_FIELD_NUMBER: _ClassVar[int]
    RECOMMEND_FANTASY_LIST_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    des: _table_basic_pb2.mlstring
    recommended_type: int
    recommend_fantasy_list: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., recommended_type: _Optional[int] = ..., recommend_fantasy_list: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class FantasySolutionTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FantasySolutionTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FantasySolutionTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FantasySolutionTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FantasySolutionTableBase]] = ...) -> None: ...
