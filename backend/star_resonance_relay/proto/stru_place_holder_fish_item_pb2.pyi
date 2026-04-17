from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlaceHolderFishItem(_message.Message):
    __slots__ = ("fish_id", "size")
    FISH_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    fish_id: int
    size: int
    def __init__(self, fish_id: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...
