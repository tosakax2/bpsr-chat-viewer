from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UnionResource(_message.Message):
    __slots__ = ("sum_num", "timer_limit_num")
    SUM_NUM_FIELD_NUMBER: _ClassVar[int]
    TIMER_LIMIT_NUM_FIELD_NUMBER: _ClassVar[int]
    sum_num: int
    timer_limit_num: int
    def __init__(self, sum_num: _Optional[int] = ..., timer_limit_num: _Optional[int] = ...) -> None: ...
