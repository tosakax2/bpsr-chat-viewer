from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReforgeKeyParam(_message.Message):
    __slots__ = ("item_uuid",)
    ITEM_UUID_FIELD_NUMBER: _ClassVar[int]
    item_uuid: int
    def __init__(self, item_uuid: _Optional[int] = ...) -> None: ...
