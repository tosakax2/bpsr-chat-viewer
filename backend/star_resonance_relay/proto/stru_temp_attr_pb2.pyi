from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TempAttr(_message.Message):
    __slots__ = ("Id", "Value")
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Id: int
    Value: int
    def __init__(self, Id: _Optional[int] = ..., Value: _Optional[int] = ...) -> None: ...
