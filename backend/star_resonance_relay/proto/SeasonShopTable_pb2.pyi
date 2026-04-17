import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonShopTableBase(_message.Message):
    __slots__ = ("id", "function_id", "name", "name_remark", "shop_type", "timer_id", "sort", "icon", "currency_display")
    ID_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_REMARK_FIELD_NUMBER: _ClassVar[int]
    SHOP_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMER_ID_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    id: int
    function_id: int
    name: _table_basic_pb2.mlstring
    name_remark: str
    shop_type: int
    timer_id: int
    sort: int
    icon: str
    currency_display: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., function_id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., name_remark: _Optional[str] = ..., shop_type: _Optional[int] = ..., timer_id: _Optional[int] = ..., sort: _Optional[int] = ..., icon: _Optional[str] = ..., currency_display: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class SeasonShopTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SeasonShopTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SeasonShopTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, SeasonShopTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, SeasonShopTableBase]] = ...) -> None: ...
