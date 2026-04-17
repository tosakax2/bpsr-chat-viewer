from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CollectingItem(_message.Message):
    __slots__ = ("item_id", "collected_num", "collect_price", "is_high")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTED_NUM_FIELD_NUMBER: _ClassVar[int]
    COLLECT_PRICE_FIELD_NUMBER: _ClassVar[int]
    IS_HIGH_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    collected_num: int
    collect_price: int
    is_high: bool
    def __init__(self, item_id: _Optional[int] = ..., collected_num: _Optional[int] = ..., collect_price: _Optional[int] = ..., is_high: bool = ...) -> None: ...
