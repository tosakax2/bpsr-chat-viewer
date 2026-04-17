import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_exchange_sell_item_data_pb2 as _stru_exchange_sell_item_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeSellItemReply(_message.Message):
    __slots__ = ("items", "with_draw_item", "limit", "rate", "err_code")
    class WithDrawItemEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    WITH_DRAW_ITEM_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_stru_exchange_sell_item_data_pb2.ExchangeSellItemData]
    with_draw_item: _containers.ScalarMap[int, int]
    limit: int
    rate: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, items: _Optional[_Iterable[_Union[_stru_exchange_sell_item_data_pb2.ExchangeSellItemData, _Mapping]]] = ..., with_draw_item: _Optional[_Mapping[int, int]] = ..., limit: _Optional[int] = ..., rate: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
