from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RewardPersonalFriendlinessLvRequest(_message.Message):
    __slots__ = ("friend_id", "level")
    FRIEND_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    friend_id: int
    level: int
    def __init__(self, friend_id: _Optional[int] = ..., level: _Optional[int] = ...) -> None: ...
