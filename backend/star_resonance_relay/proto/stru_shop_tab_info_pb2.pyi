import stru_shop_item_info_pb2 as _stru_shop_item_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShopTabInfo(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_stru_shop_item_info_pb2.ShopItemInfo]
    def __init__(self, items: _Optional[_Iterable[_Union[_stru_shop_item_info_pb2.ShopItemInfo, _Mapping]]] = ...) -> None: ...
