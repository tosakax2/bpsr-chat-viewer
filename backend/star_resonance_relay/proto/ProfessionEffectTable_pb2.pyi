import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProfessionEffectTableBase(_message.Message):
    __slots__ = ("id", "name", "short_description", "description", "arrtr_id", "value_range", "sign_id", "res_type", "buffs", "arrtrs", "normal_lib_id", "pro_lib_id", "if_close")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHORT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ARRTR_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_RANGE_FIELD_NUMBER: _ClassVar[int]
    SIGN_ID_FIELD_NUMBER: _ClassVar[int]
    RES_TYPE_FIELD_NUMBER: _ClassVar[int]
    BUFFS_FIELD_NUMBER: _ClassVar[int]
    ARRTRS_FIELD_NUMBER: _ClassVar[int]
    NORMAL_LIB_ID_FIELD_NUMBER: _ClassVar[int]
    PRO_LIB_ID_FIELD_NUMBER: _ClassVar[int]
    IF_CLOSE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    short_description: _table_basic_pb2.mlstring
    description: _table_basic_pb2.mlstring
    arrtr_id: _table_basic_pb2.int_array
    value_range: _table_basic_pb2.int_array
    sign_id: _table_basic_pb2.int_table
    res_type: int
    buffs: _table_basic_pb2.int_array
    arrtrs: _table_basic_pb2.int_table
    normal_lib_id: int
    pro_lib_id: int
    if_close: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., short_description: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., description: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., arrtr_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., value_range: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., sign_id: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., res_type: _Optional[int] = ..., buffs: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., arrtrs: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., normal_lib_id: _Optional[int] = ..., pro_lib_id: _Optional[int] = ..., if_close: bool = ...) -> None: ...

class ProfessionEffectTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ProfessionEffectTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ProfessionEffectTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ProfessionEffectTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ProfessionEffectTableBase]] = ...) -> None: ...
