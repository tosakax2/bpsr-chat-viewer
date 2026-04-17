from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyLeaveTeamRequest(_message.Message):
    __slots__ = ("char_id", "leave_type")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    LEAVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    leave_type: int
    def __init__(self, char_id: _Optional[int] = ..., leave_type: _Optional[int] = ...) -> None: ...
