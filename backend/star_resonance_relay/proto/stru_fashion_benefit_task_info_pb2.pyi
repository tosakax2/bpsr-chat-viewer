from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FashionBenefitTaskInfo(_message.Message):
    __slots__ = ("id", "count", "progress")
    ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    id: int
    count: int
    progress: int
    def __init__(self, id: _Optional[int] = ..., count: _Optional[int] = ..., progress: _Optional[int] = ...) -> None: ...
