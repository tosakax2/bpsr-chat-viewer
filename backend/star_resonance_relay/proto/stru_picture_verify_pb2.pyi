from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PictureVerify(_message.Message):
    __slots__ = ("size", "review_start_time", "version")
    SIZE_FIELD_NUMBER: _ClassVar[int]
    REVIEW_START_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    size: int
    review_start_time: int
    version: int
    def __init__(self, size: _Optional[int] = ..., review_start_time: _Optional[int] = ..., version: _Optional[int] = ...) -> None: ...
