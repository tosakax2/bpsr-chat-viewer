import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentTableBase(_message.Message):
    __slots__ = ("id", "product_name", "desc", "product_type", "currency", "price", "award_id", "items", "mail_id", "platform", "is_sale")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    MAIL_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    IS_SALE_FIELD_NUMBER: _ClassVar[int]
    id: int
    product_name: str
    desc: str
    product_type: int
    currency: str
    price: int
    award_id: int
    items: _table_basic_pb2.int_table
    mail_id: int
    platform: int
    is_sale: int
    def __init__(self, id: _Optional[int] = ..., product_name: _Optional[str] = ..., desc: _Optional[str] = ..., product_type: _Optional[int] = ..., currency: _Optional[str] = ..., price: _Optional[int] = ..., award_id: _Optional[int] = ..., items: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., mail_id: _Optional[int] = ..., platform: _Optional[int] = ..., is_sale: _Optional[int] = ...) -> None: ...

class PaymentTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: PaymentTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[PaymentTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, PaymentTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, PaymentTableBase]] = ...) -> None: ...
