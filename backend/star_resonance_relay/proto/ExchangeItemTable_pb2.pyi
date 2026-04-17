import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeItemTableBase(_message.Message):
    __slots__ = ("id", "exchange_id", "get_item_id", "get_num", "name", "consumable_id", "unlock_conditions", "refresh_type", "refresh_num", "sex_limit", "sort")
    ID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    GET_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    GET_NUM_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONSUMABLE_ID_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TYPE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_NUM_FIELD_NUMBER: _ClassVar[int]
    SEX_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    id: int
    exchange_id: int
    get_item_id: int
    get_num: int
    name: str
    consumable_id: _table_basic_pb2.int_table
    unlock_conditions: str
    refresh_type: int
    refresh_num: int
    sex_limit: int
    sort: int
    def __init__(self, id: _Optional[int] = ..., exchange_id: _Optional[int] = ..., get_item_id: _Optional[int] = ..., get_num: _Optional[int] = ..., name: _Optional[str] = ..., consumable_id: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., unlock_conditions: _Optional[str] = ..., refresh_type: _Optional[int] = ..., refresh_num: _Optional[int] = ..., sex_limit: _Optional[int] = ..., sort: _Optional[int] = ...) -> None: ...

class ExchangeItemTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ExchangeItemTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ExchangeItemTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ExchangeItemTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ExchangeItemTableBase]] = ...) -> None: ...
