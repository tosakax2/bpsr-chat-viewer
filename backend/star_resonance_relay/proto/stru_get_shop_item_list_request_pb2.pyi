from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetShopItemListRequest(_message.Message):
    __slots__ = ("shop_id",)
    SHOP_ID_FIELD_NUMBER: _ClassVar[int]
    shop_id: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, shop_id: _Optional[_Iterable[int]] = ...) -> None: ...
