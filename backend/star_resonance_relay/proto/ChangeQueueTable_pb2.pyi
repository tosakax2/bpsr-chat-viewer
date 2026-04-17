import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeQueueTableBase(_message.Message):
    __slots__ = ("id", "sort", "consumable", "consumable_name", "exchange_goods", "exchange_name", "condition", "wait_time")
    ID_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    CONSUMABLE_FIELD_NUMBER: _ClassVar[int]
    CONSUMABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_GOODS_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    WAIT_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    sort: int
    consumable: _table_basic_pb2.int_table
    consumable_name: str
    exchange_goods: _table_basic_pb2.int_table
    exchange_name: str
    condition: _table_basic_pb2.int_table
    wait_time: _table_basic_pb2.int_array
    def __init__(self, id: _Optional[int] = ..., sort: _Optional[int] = ..., consumable: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., consumable_name: _Optional[str] = ..., exchange_goods: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., exchange_name: _Optional[str] = ..., condition: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., wait_time: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ...) -> None: ...

class ChangeQueueTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ChangeQueueTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ChangeQueueTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ChangeQueueTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ChangeQueueTableBase]] = ...) -> None: ...
