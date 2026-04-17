from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyRefuseInviteRequest(_message.Message):
    __slots__ = ("invitees_name", "invitees_id")
    INVITEES_NAME_FIELD_NUMBER: _ClassVar[int]
    INVITEES_ID_FIELD_NUMBER: _ClassVar[int]
    invitees_name: str
    invitees_id: int
    def __init__(self, invitees_name: _Optional[str] = ..., invitees_id: _Optional[int] = ...) -> None: ...
