from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeSaleRequest(_message.Message):
    __slots__ = ("num", "rate")
    NUM_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    num: int
    rate: int
    def __init__(self, num: _Optional[int] = ..., rate: _Optional[int] = ...) -> None: ...
