from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyInviteJoinDungeonsRequest(_message.Message):
    __slots__ = ("group_key", "dungeon_id", "sender_id")
    GROUP_KEY_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    group_key: str
    dungeon_id: int
    sender_id: int
    def __init__(self, group_key: _Optional[str] = ..., dungeon_id: _Optional[int] = ..., sender_id: _Optional[int] = ...) -> None: ...
