from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetFishRankTopRequest(_message.Message):
    __slots__ = ("fish_area_id",)
    FISH_AREA_ID_FIELD_NUMBER: _ClassVar[int]
    fish_area_id: int
    def __init__(self, fish_area_id: _Optional[int] = ...) -> None: ...
