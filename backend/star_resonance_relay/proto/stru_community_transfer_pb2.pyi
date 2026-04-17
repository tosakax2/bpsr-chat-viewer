from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityTransfer(_message.Message):
    __slots__ = ("char_id", "time", "last_time")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_TIME_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    time: int
    last_time: int
    def __init__(self, char_id: _Optional[int] = ..., time: _Optional[int] = ..., last_time: _Optional[int] = ...) -> None: ...
