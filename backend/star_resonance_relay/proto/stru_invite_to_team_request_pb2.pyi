from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InviteToTeamRequest(_message.Message):
    __slots__ = ("invitee_char_id",)
    INVITEE_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    invitee_char_id: int
    def __init__(self, invitee_char_id: _Optional[int] = ...) -> None: ...
