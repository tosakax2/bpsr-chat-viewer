import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_exchange_sale_data_item_data_pb2 as _stru_exchange_sale_data_item_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeSaleDataReply(_message.Message):
    __slots__ = ("items", "min_rate", "err_code")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    MIN_RATE_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_stru_exchange_sale_data_item_data_pb2.ExchangeSaleDataItemData]
    min_rate: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, items: _Optional[_Iterable[_Union[_stru_exchange_sale_data_item_data_pb2.ExchangeSaleDataItemData, _Mapping]]] = ..., min_rate: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
