from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeSaleDataItemData(_message.Message):
    __slots__ = ("guid", "num", "rate", "end_time")
    GUID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    guid: str
    num: int
    rate: int
    end_time: int
    def __init__(self, guid: _Optional[str] = ..., num: _Optional[int] = ..., rate: _Optional[int] = ..., end_time: _Optional[int] = ...) -> None: ...
