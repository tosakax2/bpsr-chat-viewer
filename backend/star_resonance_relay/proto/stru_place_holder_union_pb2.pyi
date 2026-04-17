from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlaceHolderUnion(_message.Message):
    __slots__ = ("build",)
    BUILD_FIELD_NUMBER: _ClassVar[int]
    build: int
    def __init__(self, build: _Optional[int] = ...) -> None: ...
