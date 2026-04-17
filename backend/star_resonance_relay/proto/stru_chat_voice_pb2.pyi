from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChatVoice(_message.Message):
    __slots__ = ("file_id", "text", "seconds")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    text: str
    seconds: int
    def __init__(self, file_id: _Optional[str] = ..., text: _Optional[str] = ..., seconds: _Optional[int] = ...) -> None: ...
