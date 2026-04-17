from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FishingSetBaitRequest(_message.Message):
    __slots__ = ("bait_id",)
    BAIT_ID_FIELD_NUMBER: _ClassVar[int]
    bait_id: int
    def __init__(self, bait_id: _Optional[int] = ...) -> None: ...
