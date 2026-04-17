from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReJectUnionInviteRequest(_message.Message):
    __slots__ = ("invite_id",)
    INVITE_ID_FIELD_NUMBER: _ClassVar[int]
    invite_id: int
    def __init__(self, invite_id: _Optional[int] = ...) -> None: ...
