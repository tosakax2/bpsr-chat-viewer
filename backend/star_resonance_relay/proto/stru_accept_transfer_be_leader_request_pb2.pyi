from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AcceptTransferBeLeaderRequest(_message.Message):
    __slots__ = ("agree",)
    AGREE_FIELD_NUMBER: _ClassVar[int]
    agree: bool
    def __init__(self, agree: bool = ...) -> None: ...
