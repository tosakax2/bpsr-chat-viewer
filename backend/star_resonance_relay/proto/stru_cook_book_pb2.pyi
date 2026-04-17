from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CookBook(_message.Message):
    __slots__ = ("create_time",)
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: int
    def __init__(self, create_time: _Optional[int] = ...) -> None: ...
