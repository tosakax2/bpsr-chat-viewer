from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyBeMutedRequest(_message.Message):
    __slots__ = ("is_ban", "end_timestamp", "ban_reason")
    IS_BAN_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    BAN_REASON_FIELD_NUMBER: _ClassVar[int]
    is_ban: bool
    end_timestamp: int
    ban_reason: int
    def __init__(self, is_ban: bool = ..., end_timestamp: _Optional[int] = ..., ban_reason: _Optional[int] = ...) -> None: ...
