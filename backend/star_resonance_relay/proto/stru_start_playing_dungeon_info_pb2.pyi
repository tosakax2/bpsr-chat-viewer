from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StartPlayingDungeonInfo(_message.Message):
    __slots__ = ("is_use_key",)
    IS_USE_KEY_FIELD_NUMBER: _ClassVar[int]
    is_use_key: bool
    def __init__(self, is_use_key: bool = ...) -> None: ...
