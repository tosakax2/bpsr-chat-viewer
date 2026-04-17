from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityQuitCohabitant(_message.Message):
    __slots__ = ("is_initiative_quit", "time")
    IS_INITIATIVE_QUIT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    is_initiative_quit: bool
    time: int
    def __init__(self, is_initiative_quit: bool = ..., time: _Optional[int] = ...) -> None: ...
