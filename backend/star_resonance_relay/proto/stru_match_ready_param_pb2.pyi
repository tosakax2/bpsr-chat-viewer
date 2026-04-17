from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MatchReadyParam(_message.Message):
    __slots__ = ("is_ready", "match_token")
    IS_READY_FIELD_NUMBER: _ClassVar[int]
    MATCH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    is_ready: bool
    match_token: str
    def __init__(self, is_ready: bool = ..., match_token: _Optional[str] = ...) -> None: ...
