from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UninstallModRequest(_message.Message):
    __slots__ = ("slot_id",)
    SLOT_ID_FIELD_NUMBER: _ClassVar[int]
    slot_id: int
    def __init__(self, slot_id: _Optional[int] = ...) -> None: ...
