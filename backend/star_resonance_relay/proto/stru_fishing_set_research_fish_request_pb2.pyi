from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FishingSetResearchFishRequest(_message.Message):
    __slots__ = ("fish_id",)
    FISH_ID_FIELD_NUMBER: _ClassVar[int]
    fish_id: int
    def __init__(self, fish_id: _Optional[int] = ...) -> None: ...
