import enum_e_pay_type_pb2 as _enum_e_pay_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PayRequest(_message.Message):
    __slots__ = ("pay_type", "product_id", "receipt", "ext_data")
    PAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_FIELD_NUMBER: _ClassVar[int]
    EXT_DATA_FIELD_NUMBER: _ClassVar[int]
    pay_type: _enum_e_pay_type_pb2.EPayType
    product_id: int
    receipt: str
    ext_data: str
    def __init__(self, pay_type: _Optional[_Union[_enum_e_pay_type_pb2.EPayType, str]] = ..., product_id: _Optional[int] = ..., receipt: _Optional[str] = ..., ext_data: _Optional[str] = ...) -> None: ...
