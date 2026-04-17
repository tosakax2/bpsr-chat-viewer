from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BossProgress(_message.Message):
    __slots__ = ("total_award_cnt",)
    TOTAL_AWARD_CNT_FIELD_NUMBER: _ClassVar[int]
    total_award_cnt: int
    def __init__(self, total_award_cnt: _Optional[int] = ...) -> None: ...
