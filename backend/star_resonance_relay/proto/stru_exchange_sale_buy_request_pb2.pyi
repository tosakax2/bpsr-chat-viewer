from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeSaleBuyRequest(_message.Message):
    __slots__ = ("rate", "num", "else_rate")
    RATE_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    ELSE_RATE_FIELD_NUMBER: _ClassVar[int]
    rate: int
    num: int
    else_rate: int
    def __init__(self, rate: _Optional[int] = ..., num: _Optional[int] = ..., else_rate: _Optional[int] = ...) -> None: ...
