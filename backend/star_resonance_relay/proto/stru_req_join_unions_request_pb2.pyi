from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReqJoinUnionsRequest(_message.Message):
    __slots__ = ("union_ids", "is_all")
    UNION_IDS_FIELD_NUMBER: _ClassVar[int]
    IS_ALL_FIELD_NUMBER: _ClassVar[int]
    union_ids: _containers.RepeatedScalarFieldContainer[int]
    is_all: bool
    def __init__(self, union_ids: _Optional[_Iterable[int]] = ..., is_all: bool = ...) -> None: ...
