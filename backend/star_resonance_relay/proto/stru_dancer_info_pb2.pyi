from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DancerInfo(_message.Message):
    __slots__ = ("char_id", "dance_secs", "is_dancing", "has_drawn", "has_send")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    DANCE_SECS_FIELD_NUMBER: _ClassVar[int]
    IS_DANCING_FIELD_NUMBER: _ClassVar[int]
    HAS_DRAWN_FIELD_NUMBER: _ClassVar[int]
    HAS_SEND_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    dance_secs: int
    is_dancing: bool
    has_drawn: bool
    has_send: bool
    def __init__(self, char_id: _Optional[int] = ..., dance_secs: _Optional[int] = ..., is_dancing: bool = ..., has_drawn: bool = ..., has_send: bool = ...) -> None: ...
