import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MallTableBase(_message.Message):
    __slots__ = ("id", "function_id", "name", "name_remark", "has_father_type", "mall_type", "refresh_interval_type", "weight_id", "timer_id", "sort", "show_count_down", "mall_manual_refresh", "refresh_cost_item", "icon", "currency_display")
    ID_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_REMARK_FIELD_NUMBER: _ClassVar[int]
    HAS_FATHER_TYPE_FIELD_NUMBER: _ClassVar[int]
    MALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_INTERVAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    TIMER_ID_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    SHOW_COUNT_DOWN_FIELD_NUMBER: _ClassVar[int]
    MALL_MANUAL_REFRESH_FIELD_NUMBER: _ClassVar[int]
    REFRESH_COST_ITEM_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    id: int
    function_id: int
    name: _table_basic_pb2.mlstring
    name_remark: str
    has_father_type: int
    mall_type: int
    refresh_interval_type: _table_basic_pb2.int_table
    weight_id: _table_basic_pb2.int_table
    timer_id: int
    sort: int
    show_count_down: int
    mall_manual_refresh: int
    refresh_cost_item: _table_basic_pb2.int_table
    icon: str
    currency_display: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., function_id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., name_remark: _Optional[str] = ..., has_father_type: _Optional[int] = ..., mall_type: _Optional[int] = ..., refresh_interval_type: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., weight_id: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., timer_id: _Optional[int] = ..., sort: _Optional[int] = ..., show_count_down: _Optional[int] = ..., mall_manual_refresh: _Optional[int] = ..., refresh_cost_item: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., icon: _Optional[str] = ..., currency_display: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class MallTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MallTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MallTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MallTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MallTableBase]] = ...) -> None: ...
