import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MallItemTableBase(_message.Message):
    __slots__ = ("id", "item_id", "quantity", "item_name", "sort", "function_id", "limit_sex", "limit_level", "limit_time", "show_limit_type", "original_price", "cost", "refresh_type", "bind", "deliver_way", "label", "show_count_down", "weight_pool_parameter", "weight", "check_display")
    class CostEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_SEX_FIELD_NUMBER: _ClassVar[int]
    LIMIT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    LIMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    SHOW_LIMIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TYPE_FIELD_NUMBER: _ClassVar[int]
    BIND_FIELD_NUMBER: _ClassVar[int]
    DELIVER_WAY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    SHOW_COUNT_DOWN_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_POOL_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    CHECK_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    id: int
    item_id: int
    quantity: int
    item_name: str
    sort: int
    function_id: int
    limit_sex: int
    limit_level: int
    limit_time: int
    show_limit_type: _table_basic_pb2.int_table
    original_price: _table_basic_pb2.int_array
    cost: _containers.ScalarMap[int, int]
    refresh_type: _table_basic_pb2.int_table
    bind: int
    deliver_way: _table_basic_pb2.int_table
    label: _table_basic_pb2.string_array
    show_count_down: _table_basic_pb2.string_array
    weight_pool_parameter: _table_basic_pb2.int_table
    weight: _table_basic_pb2.int_table
    check_display: int
    def __init__(self, id: _Optional[int] = ..., item_id: _Optional[int] = ..., quantity: _Optional[int] = ..., item_name: _Optional[str] = ..., sort: _Optional[int] = ..., function_id: _Optional[int] = ..., limit_sex: _Optional[int] = ..., limit_level: _Optional[int] = ..., limit_time: _Optional[int] = ..., show_limit_type: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., original_price: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., cost: _Optional[_Mapping[int, int]] = ..., refresh_type: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., bind: _Optional[int] = ..., deliver_way: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., label: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., show_count_down: _Optional[_Union[_table_basic_pb2.string_array, _Mapping]] = ..., weight_pool_parameter: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., weight: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., check_display: _Optional[int] = ...) -> None: ...

class MallItemTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MallItemTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MallItemTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, MallItemTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, MallItemTableBase]] = ...) -> None: ...
