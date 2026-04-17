import enum_e_pay_type_pb2 as _enum_e_pay_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryProductRequest(_message.Message):
    __slots__ = ("pay_type",)
    PAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    pay_type: _enum_e_pay_type_pb2.EPayType
    def __init__(self, pay_type: _Optional[_Union[_enum_e_pay_type_pb2.EPayType, str]] = ...) -> None: ...
