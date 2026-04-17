from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetGroupSortRequest(_message.Message):
    __slots__ = ("group_sort",)
    GROUP_SORT_FIELD_NUMBER: _ClassVar[int]
    group_sort: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, group_sort: _Optional[_Iterable[int]] = ...) -> None: ...
