from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlaceHolderBuff(_message.Message):
    __slots__ = ("buff_id",)
    BUFF_ID_FIELD_NUMBER: _ClassVar[int]
    buff_id: int
    def __init__(self, buff_id: _Optional[int] = ...) -> None: ...
