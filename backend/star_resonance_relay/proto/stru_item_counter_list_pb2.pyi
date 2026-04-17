import stru_item_counter_info_pb2 as _stru_item_counter_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ItemCounterList(_message.Message):
    __slots__ = ("item_counter_map",)
    class ItemCounterMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_item_counter_info_pb2.ItemCounterInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_item_counter_info_pb2.ItemCounterInfo, _Mapping]] = ...) -> None: ...
    ITEM_COUNTER_MAP_FIELD_NUMBER: _ClassVar[int]
    item_counter_map: _containers.MessageMap[int, _stru_item_counter_info_pb2.ItemCounterInfo]
    def __init__(self, item_counter_map: _Optional[_Mapping[int, _stru_item_counter_info_pb2.ItemCounterInfo]] = ...) -> None: ...
