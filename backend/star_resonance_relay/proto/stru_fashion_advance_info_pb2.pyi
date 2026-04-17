from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FashionAdvanceInfo(_message.Message):
    __slots__ = ("fashion_id", "using_advance_id", "advance_ids")
    FASHION_ID_FIELD_NUMBER: _ClassVar[int]
    USING_ADVANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ADVANCE_IDS_FIELD_NUMBER: _ClassVar[int]
    fashion_id: int
    using_advance_id: int
    advance_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, fashion_id: _Optional[int] = ..., using_advance_id: _Optional[int] = ..., advance_ids: _Optional[_Iterable[int]] = ...) -> None: ...
