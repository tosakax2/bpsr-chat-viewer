from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RecruitInfo(_message.Message):
    __slots__ = ("join_level", "instruction")
    JOIN_LEVEL_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    join_level: int
    instruction: str
    def __init__(self, join_level: _Optional[int] = ..., instruction: _Optional[str] = ...) -> None: ...
