from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnionHistoryActive(_message.Message):
    __slots__ = ("union_id", "active_points")
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_POINTS_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    active_points: int
    def __init__(self, union_id: _Optional[int] = ..., active_points: _Optional[int] = ...) -> None: ...
