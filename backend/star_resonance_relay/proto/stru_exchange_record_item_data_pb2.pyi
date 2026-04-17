import enum_e_exchange_pre_item_result_pb2 as _enum_e_exchange_pre_item_result_pb2
import stru_item_pb2 as _stru_item_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeRecordItemData(_message.Message):
    __slots__ = ("config_id", "num", "price", "time", "pre_result", "item_info")
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    PRE_RESULT_FIELD_NUMBER: _ClassVar[int]
    ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
    config_id: int
    num: int
    price: int
    time: int
    pre_result: _enum_e_exchange_pre_item_result_pb2.EExchangePreItemResult
    item_info: _stru_item_pb2.Item
    def __init__(self, config_id: _Optional[int] = ..., num: _Optional[int] = ..., price: _Optional[int] = ..., time: _Optional[int] = ..., pre_result: _Optional[_Union[_enum_e_exchange_pre_item_result_pb2.EExchangePreItemResult, str]] = ..., item_info: _Optional[_Union[_stru_item_pb2.Item, _Mapping]] = ...) -> None: ...
