from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeSellItemRequest(_message.Message):
    __slots__ = ("month_card_valid",)
    MONTH_CARD_VALID_FIELD_NUMBER: _ClassVar[int]
    month_card_valid: bool
    def __init__(self, month_card_valid: bool = ...) -> None: ...
