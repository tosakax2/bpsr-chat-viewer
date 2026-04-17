from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HateInfo(_message.Message):
    __slots__ = ("uuid", "hate_val")
    UUID_FIELD_NUMBER: _ClassVar[int]
    HATE_VAL_FIELD_NUMBER: _ClassVar[int]
    uuid: int
    hate_val: int
    def __init__(self, uuid: _Optional[int] = ..., hate_val: _Optional[int] = ...) -> None: ...
