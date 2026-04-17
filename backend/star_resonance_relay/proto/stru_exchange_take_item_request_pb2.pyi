from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeTakeItemRequest(_message.Message):
    __slots__ = ("uuid", "config_id")
    UUID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    config_id: int
    def __init__(self, uuid: _Optional[str] = ..., config_id: _Optional[int] = ...) -> None: ...
