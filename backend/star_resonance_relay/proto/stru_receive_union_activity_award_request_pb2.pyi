from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReceiveUnionActivityAwardRequest(_message.Message):
    __slots__ = ("union_id", "award_id", "last_refresh_time")
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    award_id: int
    last_refresh_time: int
    def __init__(self, union_id: _Optional[int] = ..., award_id: _Optional[int] = ..., last_refresh_time: _Optional[int] = ...) -> None: ...
