from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BuyShopItemInfo(_message.Message):
    __slots__ = ("buy_num", "coupon_info")
    class CouponInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    BUY_NUM_FIELD_NUMBER: _ClassVar[int]
    COUPON_INFO_FIELD_NUMBER: _ClassVar[int]
    buy_num: int
    coupon_info: _containers.ScalarMap[int, int]
    def __init__(self, buy_num: _Optional[int] = ..., coupon_info: _Optional[_Mapping[int, int]] = ...) -> None: ...
