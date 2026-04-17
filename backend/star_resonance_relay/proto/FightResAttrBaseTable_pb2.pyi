import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FightResAttrBaseTableBase(_message.Message):
    __slots__ = ("id", "res_i_ds")
    ID_FIELD_NUMBER: _ClassVar[int]
    RES_I_DS_FIELD_NUMBER: _ClassVar[int]
    id: int
    res_i_ds: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., res_i_ds: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class FightResAttrBaseTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FightResAttrBaseTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FightResAttrBaseTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, FightResAttrBaseTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, FightResAttrBaseTableBase]] = ...) -> None: ...
