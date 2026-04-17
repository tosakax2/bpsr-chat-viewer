from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MapAttrValue(_message.Message):
    __slots__ = ("IsRemove", "Key", "Value")
    ISREMOVE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    IsRemove: bool
    Key: bytes
    Value: bytes
    def __init__(self, IsRemove: bool = ..., Key: _Optional[bytes] = ..., Value: _Optional[bytes] = ...) -> None: ...
