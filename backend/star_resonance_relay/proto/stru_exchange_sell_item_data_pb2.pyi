import enum_e_exchange_item_state_pb2 as _enum_e_exchange_item_state_pb2
import stru_item_pb2 as _stru_item_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeSellItemData(_message.Message):
    __slots__ = ("item_info", "withdraw_type", "delay_time", "uuid", "end_time", "price", "state")
    ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
    WITHDRAW_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELAY_TIME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    item_info: _stru_item_pb2.Item
    withdraw_type: int
    delay_time: int
    uuid: str
    end_time: int
    price: int
    state: _enum_e_exchange_item_state_pb2.EExchangeItemState
    def __init__(self, item_info: _Optional[_Union[_stru_item_pb2.Item, _Mapping]] = ..., withdraw_type: _Optional[int] = ..., delay_time: _Optional[int] = ..., uuid: _Optional[str] = ..., end_time: _Optional[int] = ..., price: _Optional[int] = ..., state: _Optional[_Union[_enum_e_exchange_item_state_pb2.EExchangeItemState, str]] = ...) -> None: ...
