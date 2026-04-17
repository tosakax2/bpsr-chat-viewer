import stru_item_pb2 as _stru_item_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangePriceItemData(_message.Message):
    __slots__ = ("price", "num", "item_info", "guid", "notice_time")
    PRICE_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
    GUID_FIELD_NUMBER: _ClassVar[int]
    NOTICE_TIME_FIELD_NUMBER: _ClassVar[int]
    price: int
    num: int
    item_info: _stru_item_pb2.Item
    guid: str
    notice_time: int
    def __init__(self, price: _Optional[int] = ..., num: _Optional[int] = ..., item_info: _Optional[_Union[_stru_item_pb2.Item, _Mapping]] = ..., guid: _Optional[str] = ..., notice_time: _Optional[int] = ...) -> None: ...
