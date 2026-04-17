import enum_e_exchange_item_type_pb2 as _enum_e_exchange_item_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeCareListRequest(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _enum_e_exchange_item_type_pb2.EExchangeItemType
    def __init__(self, type: _Optional[_Union[_enum_e_exchange_item_type_pb2.EExchangeItemType, str]] = ...) -> None: ...
