import stru_item_pb2 as _stru_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonAward(_message.Message):
    __slots__ = ("items", "flag_assist", "award_count", "first_items")
    class ItemsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_item_pb2.Item
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_item_pb2.Item, _Mapping]] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    FLAG_ASSIST_FIELD_NUMBER: _ClassVar[int]
    AWARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    FIRST_ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.MessageMap[int, _stru_item_pb2.Item]
    flag_assist: int
    award_count: int
    first_items: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, items: _Optional[_Mapping[int, _stru_item_pb2.Item]] = ..., flag_assist: _Optional[int] = ..., award_count: _Optional[int] = ..., first_items: _Optional[_Iterable[int]] = ...) -> None: ...
