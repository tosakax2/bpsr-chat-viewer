from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RequestAddFriendRequest(_message.Message):
    __slots__ = ("char_id", "source")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    source: int
    def __init__(self, char_id: _Optional[int] = ..., source: _Optional[int] = ...) -> None: ...
