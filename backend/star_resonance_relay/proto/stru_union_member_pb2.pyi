from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnionMember(_message.Message):
    __slots__ = ("official_id", "mem_id", "join_time", "week_active_points", "history_active_points")
    OFFICIAL_ID_FIELD_NUMBER: _ClassVar[int]
    MEM_ID_FIELD_NUMBER: _ClassVar[int]
    JOIN_TIME_FIELD_NUMBER: _ClassVar[int]
    WEEK_ACTIVE_POINTS_FIELD_NUMBER: _ClassVar[int]
    HISTORY_ACTIVE_POINTS_FIELD_NUMBER: _ClassVar[int]
    official_id: int
    mem_id: int
    join_time: int
    week_active_points: int
    history_active_points: int
    def __init__(self, official_id: _Optional[int] = ..., mem_id: _Optional[int] = ..., join_time: _Optional[int] = ..., week_active_points: _Optional[int] = ..., history_active_points: _Optional[int] = ...) -> None: ...
