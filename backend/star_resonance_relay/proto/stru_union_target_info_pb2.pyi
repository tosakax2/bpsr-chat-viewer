from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnionTargetInfo(_message.Message):
    __slots__ = ("target_id", "target_num", "has_finished")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_NUM_FIELD_NUMBER: _ClassVar[int]
    HAS_FINISHED_FIELD_NUMBER: _ClassVar[int]
    target_id: int
    target_num: int
    has_finished: bool
    def __init__(self, target_id: _Optional[int] = ..., target_num: _Optional[int] = ..., has_finished: bool = ...) -> None: ...
