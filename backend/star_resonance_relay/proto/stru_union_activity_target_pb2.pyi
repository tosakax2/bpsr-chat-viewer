from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnionActivityTarget(_message.Message):
    __slots__ = ("cur_num", "has_finished", "last_refresh_time", "next_refresh_time", "target_id")
    CUR_NUM_FIELD_NUMBER: _ClassVar[int]
    HAS_FINISHED_FIELD_NUMBER: _ClassVar[int]
    LAST_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    cur_num: int
    has_finished: bool
    last_refresh_time: int
    next_refresh_time: int
    target_id: int
    def __init__(self, cur_num: _Optional[int] = ..., has_finished: bool = ..., last_refresh_time: _Optional[int] = ..., next_refresh_time: _Optional[int] = ..., target_id: _Optional[int] = ...) -> None: ...
