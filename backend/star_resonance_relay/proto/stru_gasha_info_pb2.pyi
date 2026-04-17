from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GashaInfo(_message.Message):
    __slots__ = ("id", "draw_count", "refresh_time", "wish_id", "wish_value", "wish_finish_count", "wish_reset_time", "wish_limit")
    ID_FIELD_NUMBER: _ClassVar[int]
    DRAW_COUNT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    WISH_ID_FIELD_NUMBER: _ClassVar[int]
    WISH_VALUE_FIELD_NUMBER: _ClassVar[int]
    WISH_FINISH_COUNT_FIELD_NUMBER: _ClassVar[int]
    WISH_RESET_TIME_FIELD_NUMBER: _ClassVar[int]
    WISH_LIMIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    draw_count: int
    refresh_time: int
    wish_id: int
    wish_value: int
    wish_finish_count: int
    wish_reset_time: int
    wish_limit: int
    def __init__(self, id: _Optional[int] = ..., draw_count: _Optional[int] = ..., refresh_time: _Optional[int] = ..., wish_id: _Optional[int] = ..., wish_value: _Optional[int] = ..., wish_finish_count: _Optional[int] = ..., wish_reset_time: _Optional[int] = ..., wish_limit: _Optional[int] = ...) -> None: ...
