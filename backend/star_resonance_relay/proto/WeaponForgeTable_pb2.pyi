import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WeaponForgeTableBase(_message.Message):
    __slots__ = ("id", "name", "consumable_id", "consumable_gold", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONSUMABLE_ID_FIELD_NUMBER: _ClassVar[int]
    CONSUMABLE_GOLD_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    consumable_id: _table_basic_pb2.int_table
    consumable_gold: _table_basic_pb2.int_array
    sort: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., consumable_id: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., consumable_gold: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., sort: _Optional[int] = ...) -> None: ...

class WeaponForgeTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: WeaponForgeTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[WeaponForgeTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, WeaponForgeTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, WeaponForgeTableBase]] = ...) -> None: ...
