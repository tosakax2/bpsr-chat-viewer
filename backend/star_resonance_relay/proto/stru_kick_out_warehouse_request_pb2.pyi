from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class KickOutWarehouseRequest(_message.Message):
    __slots__ = ("kick_char_id",)
    KICK_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    kick_char_id: int
    def __init__(self, kick_char_id: _Optional[int] = ...) -> None: ...
