import stru_notify_buy_shop_item_info_pb2 as _stru_notify_buy_shop_item_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyBuyShopResultParam(_message.Message):
    __slots__ = ("err_code", "buy_shop_item_info")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    BUY_SHOP_ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
    err_code: int
    buy_shop_item_info: _containers.RepeatedCompositeFieldContainer[_stru_notify_buy_shop_item_info_pb2.NotifyBuyShopItemInfo]
    def __init__(self, err_code: _Optional[int] = ..., buy_shop_item_info: _Optional[_Iterable[_Union[_stru_notify_buy_shop_item_info_pb2.NotifyBuyShopItemInfo, _Mapping]]] = ...) -> None: ...
