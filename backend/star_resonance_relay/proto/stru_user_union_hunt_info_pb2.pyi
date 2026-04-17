from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UserUnionHuntInfo(_message.Message):
    __slots__ = ("hunt_rank",)
    HUNT_RANK_FIELD_NUMBER: _ClassVar[int]
    hunt_rank: int
    def __init__(self, hunt_rank: _Optional[int] = ...) -> None: ...
