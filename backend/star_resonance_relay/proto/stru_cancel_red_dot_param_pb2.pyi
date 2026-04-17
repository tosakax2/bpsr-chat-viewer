from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CancelRedDotParam(_message.Message):
    __slots__ = ("red_dot_id",)
    RED_DOT_ID_FIELD_NUMBER: _ClassVar[int]
    red_dot_id: int
    def __init__(self, red_dot_id: _Optional[int] = ...) -> None: ...
