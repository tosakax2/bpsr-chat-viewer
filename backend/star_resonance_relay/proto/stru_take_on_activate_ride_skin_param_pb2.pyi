from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TakeOnActivateRideSkinParam(_message.Message):
    __slots__ = ("skin_id",)
    SKIN_ID_FIELD_NUMBER: _ClassVar[int]
    skin_id: int
    def __init__(self, skin_id: _Optional[int] = ...) -> None: ...
