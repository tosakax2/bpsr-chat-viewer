from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MultiLanguageContentTextInfo(_message.Message):
    __slots__ = ("language", "content_text")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TEXT_FIELD_NUMBER: _ClassVar[int]
    language: int
    content_text: str
    def __init__(self, language: _Optional[int] = ..., content_text: _Optional[str] = ...) -> None: ...
