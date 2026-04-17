from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityUnlockFurnitureRecipeRequest(_message.Message):
    __slots__ = ("furniture_id",)
    FURNITURE_ID_FIELD_NUMBER: _ClassVar[int]
    furniture_id: int
    def __init__(self, furniture_id: _Optional[int] = ...) -> None: ...
