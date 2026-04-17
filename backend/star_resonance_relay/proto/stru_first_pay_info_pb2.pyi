from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FirstPayInfo(_message.Message):
    __slots__ = ("first_pay_type", "timestamp")
    FIRST_PAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    first_pay_type: int
    timestamp: int
    def __init__(self, first_pay_type: _Optional[int] = ..., timestamp: _Optional[int] = ...) -> None: ...
