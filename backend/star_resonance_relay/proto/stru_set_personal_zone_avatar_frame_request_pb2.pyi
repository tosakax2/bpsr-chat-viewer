from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetPersonalZoneAvatarFrameRequest(_message.Message):
    __slots__ = ("avatar_frame_id",)
    AVATAR_FRAME_ID_FIELD_NUMBER: _ClassVar[int]
    avatar_frame_id: int
    def __init__(self, avatar_frame_id: _Optional[int] = ...) -> None: ...
