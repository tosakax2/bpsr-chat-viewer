from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BeginMatchParam(_message.Message):
    __slots__ = ("target_id", "want_leader")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    WANT_LEADER_FIELD_NUMBER: _ClassVar[int]
    target_id: int
    want_leader: int
    def __init__(self, target_id: _Optional[int] = ..., want_leader: _Optional[int] = ...) -> None: ...
