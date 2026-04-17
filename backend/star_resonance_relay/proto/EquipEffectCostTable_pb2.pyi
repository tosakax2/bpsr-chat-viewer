import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EquipEffectCostTableBase(_message.Message):
    __slots__ = ("effect_type", "effect_type_name", "item_cost")
    EFFECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEM_COST_FIELD_NUMBER: _ClassVar[int]
    effect_type: int
    effect_type_name: _table_basic_pb2.mlstring
    item_cost: _table_basic_pb2.int_table
    def __init__(self, effect_type: _Optional[int] = ..., effect_type_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., item_cost: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class EquipEffectCostTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: EquipEffectCostTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[EquipEffectCostTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, EquipEffectCostTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, EquipEffectCostTableBase]] = ...) -> None: ...
