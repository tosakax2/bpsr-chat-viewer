from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CancelMatchParam(_message.Message):
    __slots__ = ("match_token",)
    MATCH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    match_token: str
    def __init__(self, match_token: _Optional[str] = ...) -> None: ...
