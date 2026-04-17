from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SyncInviteRequest(_message.Message):
    __slots__ = ("invite_id", "invite_name", "union_name", "union_id")
    INVITE_ID_FIELD_NUMBER: _ClassVar[int]
    INVITE_NAME_FIELD_NUMBER: _ClassVar[int]
    UNION_NAME_FIELD_NUMBER: _ClassVar[int]
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    invite_id: int
    invite_name: str
    union_name: str
    union_id: int
    def __init__(self, invite_id: _Optional[int] = ..., invite_name: _Optional[str] = ..., union_name: _Optional[str] = ..., union_id: _Optional[int] = ...) -> None: ...
