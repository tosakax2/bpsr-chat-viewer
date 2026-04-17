from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ShopItemBuyLimit(_message.Message):
    __slots__ = ("purchased_count", "can_buy_count", "max_buy_count")
    PURCHASED_COUNT_FIELD_NUMBER: _ClassVar[int]
    CAN_BUY_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_BUY_COUNT_FIELD_NUMBER: _ClassVar[int]
    purchased_count: int
    can_buy_count: int
    max_buy_count: int
    def __init__(self, purchased_count: _Optional[int] = ..., can_buy_count: _Optional[int] = ..., max_buy_count: _Optional[int] = ...) -> None: ...
