import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModDecomposeTableBase(_message.Message):
    __slots__ = ("id", "mod_lvl", "mod_type", "mod_decomposea", "mod_decomposeb")
    ID_FIELD_NUMBER: _ClassVar[int]
    MOD_LVL_FIELD_NUMBER: _ClassVar[int]
    MOD_TYPE_FIELD_NUMBER: _ClassVar[int]
    MOD_DECOMPOSEA_FIELD_NUMBER: _ClassVar[int]
    MOD_DECOMPOSEB_FIELD_NUMBER: _ClassVar[int]
    id: int
    mod_lvl: int
    mod_type: int
    mod_decomposea: _table_basic_pb2.int_table
    mod_decomposeb: _table_basic_pb2.int_table
    def __init__(self, id: _Optional[int] = ..., mod_lvl: _Optional[int] = ..., mod_type: _Optional[int] = ..., mod_decomposea: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., mod_decomposeb: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class ModDecomposeTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ModDecomposeTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ModDecomposeTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ModDecomposeTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ModDecomposeTableBase]] = ...) -> None: ...
