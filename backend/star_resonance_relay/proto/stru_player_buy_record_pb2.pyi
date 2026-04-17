from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerBuyRecord(_message.Message):
    __slots__ = ("count", "buy_timestamp")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    BUY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    count: int
    buy_timestamp: int
    def __init__(self, count: _Optional[int] = ..., buy_timestamp: _Optional[int] = ...) -> None: ...
