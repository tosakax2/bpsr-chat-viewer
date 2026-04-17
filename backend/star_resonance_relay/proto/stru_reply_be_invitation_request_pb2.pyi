from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReplyBeInvitationRequest(_message.Message):
    __slots__ = ("team_id", "agree")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    AGREE_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    agree: bool
    def __init__(self, team_id: _Optional[int] = ..., agree: bool = ...) -> None: ...
