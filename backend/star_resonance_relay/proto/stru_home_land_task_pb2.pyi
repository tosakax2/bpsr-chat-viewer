from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomeLandTask(_message.Message):
    __slots__ = ("finished",)
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    finished: bool
    def __init__(self, finished: bool = ...) -> None: ...
