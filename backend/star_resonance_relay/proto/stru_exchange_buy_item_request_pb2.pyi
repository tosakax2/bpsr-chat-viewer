from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeBuyItemRequest(_message.Message):
    __slots__ = ("uuid", "config_id", "num", "price")
    UUID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    config_id: int
    num: int
    price: int
    def __init__(self, uuid: _Optional[str] = ..., config_id: _Optional[int] = ..., num: _Optional[int] = ..., price: _Optional[int] = ...) -> None: ...
