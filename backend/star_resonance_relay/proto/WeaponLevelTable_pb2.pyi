import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WeaponLevelTableBase(_message.Message):
    __slots__ = ("id", "exp", "broke", "item_price", "extr_cost", "skill_max_level")
    ID_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    BROKE_FIELD_NUMBER: _ClassVar[int]
    ITEM_PRICE_FIELD_NUMBER: _ClassVar[int]
    EXTR_COST_FIELD_NUMBER: _ClassVar[int]
    SKILL_MAX_LEVEL_FIELD_NUMBER: _ClassVar[int]
    id: int
    exp: int
    broke: bool
    item_price: _table_basic_pb2.int_table
    extr_cost: _table_basic_pb2.int_table
    skill_max_level: int
    def __init__(self, id: _Optional[int] = ..., exp: _Optional[int] = ..., broke: bool = ..., item_price: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., extr_cost: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., skill_max_level: _Optional[int] = ...) -> None: ...

class WeaponLevelTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: WeaponLevelTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[WeaponLevelTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, WeaponLevelTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, WeaponLevelTableBase]] = ...) -> None: ...
