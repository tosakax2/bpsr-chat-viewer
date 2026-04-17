from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FishingSetRodRequest(_message.Message):
    __slots__ = ("rod_uuid",)
    ROD_UUID_FIELD_NUMBER: _ClassVar[int]
    rod_uuid: int
    def __init__(self, rod_uuid: _Optional[int] = ...) -> None: ...
