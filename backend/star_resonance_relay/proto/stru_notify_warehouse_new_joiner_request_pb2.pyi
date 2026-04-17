from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyWarehouseNewJoinerRequest(_message.Message):
    __slots__ = ("join_char_id",)
    JOIN_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    join_char_id: int
    def __init__(self, join_char_id: _Optional[int] = ...) -> None: ...
