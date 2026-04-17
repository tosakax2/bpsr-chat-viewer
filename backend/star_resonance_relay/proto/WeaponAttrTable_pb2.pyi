import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WeaponAttrTableBase(_message.Message):
    __slots__ = ("id", "weapon_id", "level", "base_attr", "extra_attr")
    ID_FIELD_NUMBER: _ClassVar[int]
    WEAPON_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    BASE_ATTR_FIELD_NUMBER: _ClassVar[int]
    EXTRA_ATTR_FIELD_NUMBER: _ClassVar[int]
    id: int
    weapon_id: int
    level: int
    base_attr: _table_basic_pb2.int_table
    extra_attr: _table_basic_pb2.int_table
    def __init__(self, id: _Optional[int] = ..., weapon_id: _Optional[int] = ..., level: _Optional[int] = ..., base_attr: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., extra_attr: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class WeaponAttrTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: WeaponAttrTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[WeaponAttrTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, WeaponAttrTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, WeaponAttrTableBase]] = ...) -> None: ...
