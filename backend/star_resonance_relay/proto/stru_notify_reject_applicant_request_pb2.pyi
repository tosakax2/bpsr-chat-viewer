from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyRejectApplicantRequest(_message.Message):
    __slots__ = ("leader_name", "leader_id")
    LEADER_NAME_FIELD_NUMBER: _ClassVar[int]
    LEADER_ID_FIELD_NUMBER: _ClassVar[int]
    leader_name: str
    leader_id: int
    def __init__(self, leader_name: _Optional[str] = ..., leader_id: _Optional[int] = ...) -> None: ...
