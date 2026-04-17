import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EquipEffectLibTableBase(_message.Message):
    __slots__ = ("id", "effect_lib_id", "effect_type", "element")
    ID_FIELD_NUMBER: _ClassVar[int]
    EFFECT_LIB_ID_FIELD_NUMBER: _ClassVar[int]
    EFFECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    id: int
    effect_lib_id: int
    effect_type: _table_basic_pb2.int_array
    element: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., effect_lib_id: _Optional[int] = ..., effect_type: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., element: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class EquipEffectLibTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: EquipEffectLibTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[EquipEffectLibTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, EquipEffectLibTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, EquipEffectLibTableBase]] = ...) -> None: ...
