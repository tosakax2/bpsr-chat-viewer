from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnlockCookBookInfo(_message.Message):
    __slots__ = ("book_list", "food_list")
    class FoodListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    BOOK_LIST_FIELD_NUMBER: _ClassVar[int]
    FOOD_LIST_FIELD_NUMBER: _ClassVar[int]
    book_list: _containers.RepeatedScalarFieldContainer[int]
    food_list: _containers.ScalarMap[int, int]
    def __init__(self, book_list: _Optional[_Iterable[int]] = ..., food_list: _Optional[_Mapping[int, int]] = ...) -> None: ...
