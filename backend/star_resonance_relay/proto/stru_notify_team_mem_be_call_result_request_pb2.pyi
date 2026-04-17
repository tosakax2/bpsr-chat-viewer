from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyTeamMemBeCallResultRequest(_message.Message):
    __slots__ = ("member_id", "tips_id")
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    TIPS_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: int
    tips_id: int
    def __init__(self, member_id: _Optional[int] = ..., tips_id: _Optional[int] = ...) -> None: ...
