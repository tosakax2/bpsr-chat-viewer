from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MailMultilingualText(_message.Message):
    __slots__ = ("language", "send_name", "mail_title", "mail_content")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    SEND_NAME_FIELD_NUMBER: _ClassVar[int]
    MAIL_TITLE_FIELD_NUMBER: _ClassVar[int]
    MAIL_CONTENT_FIELD_NUMBER: _ClassVar[int]
    language: int
    send_name: str
    mail_title: str
    mail_content: str
    def __init__(self, language: _Optional[int] = ..., send_name: _Optional[str] = ..., mail_title: _Optional[str] = ..., mail_content: _Optional[str] = ...) -> None: ...
