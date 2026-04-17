from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonTargetData(_message.Message):
    __slots__ = ("target_id", "nums", "complete")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    NUMS_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    target_id: int
    nums: int
    complete: int
    def __init__(self, target_id: _Optional[int] = ..., nums: _Optional[int] = ..., complete: _Optional[int] = ...) -> None: ...
