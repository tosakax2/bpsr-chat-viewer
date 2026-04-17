import stru_collecting_item_pb2 as _stru_collecting_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeLandSellShopInfo(_message.Message):
    __slots__ = ("is_init", "next_reflush_time", "collecting_items", "new_next_reflush_sec")
    class CollectingItemsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_collecting_item_pb2.CollectingItem
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_collecting_item_pb2.CollectingItem, _Mapping]] = ...) -> None: ...
    IS_INIT_FIELD_NUMBER: _ClassVar[int]
    NEXT_REFLUSH_TIME_FIELD_NUMBER: _ClassVar[int]
    COLLECTING_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEW_NEXT_REFLUSH_SEC_FIELD_NUMBER: _ClassVar[int]
    is_init: bool
    next_reflush_time: int
    collecting_items: _containers.MessageMap[int, _stru_collecting_item_pb2.CollectingItem]
    new_next_reflush_sec: int
    def __init__(self, is_init: bool = ..., next_reflush_time: _Optional[int] = ..., collecting_items: _Optional[_Mapping[int, _stru_collecting_item_pb2.CollectingItem]] = ..., new_next_reflush_sec: _Optional[int] = ...) -> None: ...
