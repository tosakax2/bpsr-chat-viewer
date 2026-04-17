import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EquipAttrLibTableBase(_message.Message):
    __slots__ = ("id", "attr_lib_id", "equip_level_range", "equip_part", "attr", "value_cal")
    ID_FIELD_NUMBER: _ClassVar[int]
    ATTR_LIB_ID_FIELD_NUMBER: _ClassVar[int]
    EQUIP_LEVEL_RANGE_FIELD_NUMBER: _ClassVar[int]
    EQUIP_PART_FIELD_NUMBER: _ClassVar[int]
    ATTR_FIELD_NUMBER: _ClassVar[int]
    VALUE_CAL_FIELD_NUMBER: _ClassVar[int]
    id: int
    attr_lib_id: int
    equip_level_range: _table_basic_pb2.int_array
    equip_part: _table_basic_pb2.int_array
    attr: _table_basic_pb2.int_array
    value_cal: _table_basic_pb2.number_table
    def __init__(self, id: _Optional[int] = ..., attr_lib_id: _Optional[int] = ..., equip_level_range: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., equip_part: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., attr: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., value_cal: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ...) -> None: ...

class EquipAttrLibTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: EquipAttrLibTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[EquipAttrLibTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, EquipAttrLibTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, EquipAttrLibTableBase]] = ...) -> None: ...
