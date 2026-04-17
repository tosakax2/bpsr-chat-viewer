from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MahjongMatchRequest(_message.Message):
    __slots__ = ("game_type",)
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    game_type: int
    def __init__(self, game_type: _Optional[int] = ...) -> None: ...
