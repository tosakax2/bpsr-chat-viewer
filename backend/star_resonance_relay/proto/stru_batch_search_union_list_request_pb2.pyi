from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BatchSearchUnionListRequest(_message.Message):
    __slots__ = ("union_id_list",)
    UNION_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    union_id_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, union_id_list: _Optional[_Iterable[int]] = ...) -> None: ...
