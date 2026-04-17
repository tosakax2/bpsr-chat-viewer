from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlaceHolderFishRank(_message.Message):
    __slots__ = ("fish_id", "size", "rank")
    FISH_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    fish_id: int
    size: int
    rank: int
    def __init__(self, fish_id: _Optional[int] = ..., size: _Optional[int] = ..., rank: _Optional[int] = ...) -> None: ...
