from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeItemInfo(_message.Message):
    __slots__ = ("config_id", "num", "min_price", "is_care")
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    MIN_PRICE_FIELD_NUMBER: _ClassVar[int]
    IS_CARE_FIELD_NUMBER: _ClassVar[int]
    config_id: int
    num: int
    min_price: int
    is_care: bool
    def __init__(self, config_id: _Optional[int] = ..., num: _Optional[int] = ..., min_price: _Optional[int] = ..., is_care: bool = ...) -> None: ...
