from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InviteJoinDungeonsRequest(_message.Message):
    __slots__ = ("invite_receiver",)
    INVITE_RECEIVER_FIELD_NUMBER: _ClassVar[int]
    invite_receiver: int
    def __init__(self, invite_receiver: _Optional[int] = ...) -> None: ...
