from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MahjongSettleMessage(_message.Message):
    __slots__ = ("confirm_index", "confirm_time")
    CONFIRM_INDEX_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_TIME_FIELD_NUMBER: _ClassVar[int]
    confirm_index: int
    confirm_time: int
    def __init__(self, confirm_index: _Optional[int] = ..., confirm_time: _Optional[int] = ...) -> None: ...
