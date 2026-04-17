import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PayFunctionTableBase(_message.Message):
    __slots__ = ("id", "payment_id", "name", "desc", "show_type", "icon", "sort", "label", "is_sale")
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    SHOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    IS_SALE_FIELD_NUMBER: _ClassVar[int]
    id: int
    payment_id: _table_basic_pb2.int_array
    name: _table_basic_pb2.mlstring
    desc: str
    show_type: int
    icon: str
    sort: int
    label: _table_basic_pb2.int_table
    is_sale: int
    def __init__(self, id: _Optional[int] = ..., payment_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., desc: _Optional[str] = ..., show_type: _Optional[int] = ..., icon: _Optional[str] = ..., sort: _Optional[int] = ..., label: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., is_sale: _Optional[int] = ...) -> None: ...

class PayFunctionTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: PayFunctionTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[PayFunctionTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, PayFunctionTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, PayFunctionTableBase]] = ...) -> None: ...
