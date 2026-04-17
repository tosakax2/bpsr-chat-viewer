from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityInvitationInfo(_message.Message):
    __slots__ = ("time", "invitee_char_id")
    TIME_FIELD_NUMBER: _ClassVar[int]
    INVITEE_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    time: int
    invitee_char_id: int
    def __init__(self, time: _Optional[int] = ..., invitee_char_id: _Optional[int] = ...) -> None: ...
