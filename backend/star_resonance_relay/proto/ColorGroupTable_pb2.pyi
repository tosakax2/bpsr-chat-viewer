import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ColorGroupTableBase(_message.Message):
    __slots__ = ("id", "type", "color", "hue", "if_saturation", "saturation", "if_value", "value", "ui_color", "consumeh", "zone", "consume_low", "consume_high", "unlock")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    HUE_FIELD_NUMBER: _ClassVar[int]
    IF_SATURATION_FIELD_NUMBER: _ClassVar[int]
    SATURATION_FIELD_NUMBER: _ClassVar[int]
    IF_VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UI_COLOR_FIELD_NUMBER: _ClassVar[int]
    CONSUMEH_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CONSUME_LOW_FIELD_NUMBER: _ClassVar[int]
    CONSUME_HIGH_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: int
    color: str
    hue: _table_basic_pb2.int_table
    if_saturation: int
    saturation: _table_basic_pb2.int_table
    if_value: int
    value: _table_basic_pb2.int_table
    ui_color: _table_basic_pb2.int_table
    consumeh: _table_basic_pb2.int_table
    zone: _table_basic_pb2.int_table
    consume_low: _table_basic_pb2.int_table
    consume_high: _table_basic_pb2.int_table
    unlock: _table_basic_pb2.int_table
    def __init__(self, id: _Optional[int] = ..., type: _Optional[int] = ..., color: _Optional[str] = ..., hue: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., if_saturation: _Optional[int] = ..., saturation: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., if_value: _Optional[int] = ..., value: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., ui_color: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., consumeh: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., zone: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., consume_low: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., consume_high: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., unlock: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ...) -> None: ...

class ColorGroupTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ColorGroupTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ColorGroupTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ColorGroupTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ColorGroupTableBase]] = ...) -> None: ...
