from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyBuyShopItemInfo(_message.Message):
    __slots__ = ("shop_id", "item_id", "buy_num", "err_code")
    SHOP_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    BUY_NUM_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    shop_id: int
    item_id: int
    buy_num: int
    err_code: int
    def __init__(self, shop_id: _Optional[int] = ..., item_id: _Optional[int] = ..., buy_num: _Optional[int] = ..., err_code: _Optional[int] = ...) -> None: ...
