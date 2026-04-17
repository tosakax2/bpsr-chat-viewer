from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LuckyValueInfo(_message.Message):
    __slots__ = ("luck_id", "luck_value", "next_time")
    LUCK_ID_FIELD_NUMBER: _ClassVar[int]
    LUCK_VALUE_FIELD_NUMBER: _ClassVar[int]
    NEXT_TIME_FIELD_NUMBER: _ClassVar[int]
    luck_id: int
    luck_value: int
    next_time: int
    def __init__(self, luck_id: _Optional[int] = ..., luck_value: _Optional[int] = ..., next_time: _Optional[int] = ...) -> None: ...
