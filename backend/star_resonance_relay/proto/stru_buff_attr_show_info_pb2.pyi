from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BuffAttrShowInfo(_message.Message):
    __slots__ = ("id", "is_gain")
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_GAIN_FIELD_NUMBER: _ClassVar[int]
    id: int
    is_gain: bool
    def __init__(self, id: _Optional[int] = ..., is_gain: bool = ...) -> None: ...
