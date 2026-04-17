from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MahjongPlayerEmojiInfo(_message.Message):
    __slots__ = ("player_id", "emoji_id")
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    EMOJI_ID_FIELD_NUMBER: _ClassVar[int]
    player_id: int
    emoji_id: int
    def __init__(self, player_id: _Optional[int] = ..., emoji_id: _Optional[int] = ...) -> None: ...
