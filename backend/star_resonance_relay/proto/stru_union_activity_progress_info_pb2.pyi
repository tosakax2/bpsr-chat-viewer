from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnionActivityProgressInfo(_message.Message):
    __slots__ = ("activity_id", "progress", "award")
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    AWARD_FIELD_NUMBER: _ClassVar[int]
    activity_id: int
    progress: int
    award: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, activity_id: _Optional[int] = ..., progress: _Optional[int] = ..., award: _Optional[_Iterable[int]] = ...) -> None: ...
