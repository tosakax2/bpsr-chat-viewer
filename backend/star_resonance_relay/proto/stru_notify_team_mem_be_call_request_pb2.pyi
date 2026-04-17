from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyTeamMemBeCallRequest(_message.Message):
    __slots__ = ("leader_id", "time")
    LEADER_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    leader_id: int
    time: int
    def __init__(self, leader_id: _Optional[int] = ..., time: _Optional[int] = ...) -> None: ...
