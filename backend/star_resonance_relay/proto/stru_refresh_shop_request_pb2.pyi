from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RefreshShopRequest(_message.Message):
    __slots__ = ("shop_id",)
    SHOP_ID_FIELD_NUMBER: _ClassVar[int]
    shop_id: int
    def __init__(self, shop_id: _Optional[int] = ...) -> None: ...
