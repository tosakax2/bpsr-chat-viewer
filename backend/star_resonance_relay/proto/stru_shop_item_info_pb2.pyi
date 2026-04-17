import stru_shop_item_buy_limit_pb2 as _stru_shop_item_buy_limit_pb2
import enum_shop_limit_buy_type_pb2 as _enum_shop_limit_buy_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShopItemInfo(_message.Message):
    __slots__ = ("item_id", "start_time", "end_time", "limit_buy_type", "buy_count")
    class BuyCountEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_shop_item_buy_limit_pb2.ShopItemBuyLimit
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_shop_item_buy_limit_pb2.ShopItemBuyLimit, _Mapping]] = ...) -> None: ...
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_BUY_TYPE_FIELD_NUMBER: _ClassVar[int]
    BUY_COUNT_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    start_time: int
    end_time: int
    limit_buy_type: _enum_shop_limit_buy_type_pb2.ShopLimitBuyType
    buy_count: _containers.MessageMap[int, _stru_shop_item_buy_limit_pb2.ShopItemBuyLimit]
    def __init__(self, item_id: _Optional[int] = ..., start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., limit_buy_type: _Optional[_Union[_enum_shop_limit_buy_type_pb2.ShopLimitBuyType, str]] = ..., buy_count: _Optional[_Mapping[int, _stru_shop_item_buy_limit_pb2.ShopItemBuyLimit]] = ...) -> None: ...
