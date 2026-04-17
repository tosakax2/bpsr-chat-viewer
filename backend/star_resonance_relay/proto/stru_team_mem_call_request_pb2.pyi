from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TeamMemCallRequest(_message.Message):
    __slots__ = ("call_status",)
    CALL_STATUS_FIELD_NUMBER: _ClassVar[int]
    call_status: int
    def __init__(self, call_status: _Optional[int] = ...) -> None: ...
