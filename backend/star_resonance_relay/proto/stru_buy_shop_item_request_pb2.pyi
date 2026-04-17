import stru_buy_shop_item_info_pb2 as _stru_buy_shop_item_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuyShopItemRequest(_message.Message):
    __slots__ = ("buy_shop_item_info", "ext_data")
    class BuyShopItemInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_buy_shop_item_info_pb2.BuyShopItemInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_buy_shop_item_info_pb2.BuyShopItemInfo, _Mapping]] = ...) -> None: ...
    BUY_SHOP_ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
    EXT_DATA_FIELD_NUMBER: _ClassVar[int]
    buy_shop_item_info: _containers.MessageMap[int, _stru_buy_shop_item_info_pb2.BuyShopItemInfo]
    ext_data: str
    def __init__(self, buy_shop_item_info: _Optional[_Mapping[int, _stru_buy_shop_item_info_pb2.BuyShopItemInfo]] = ..., ext_data: _Optional[str] = ...) -> None: ...
