from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityAcceptRejectInvitationRequest(_message.Message):
    __slots__ = ("char_id", "home_id", "accept")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    HOME_ID_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    home_id: int
    accept: bool
    def __init__(self, char_id: _Optional[int] = ..., home_id: _Optional[int] = ..., accept: bool = ...) -> None: ...
