from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChallengeDungeonScoreAwardParam(_message.Message):
    __slots__ = ("group_id", "target_id")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    target_id: int
    def __init__(self, group_id: _Optional[int] = ..., target_id: _Optional[int] = ...) -> None: ...
