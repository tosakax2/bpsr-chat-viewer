from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetQuestionnaireListRequest(_message.Message):
    __slots__ = ("level", "login_day", "language_id")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    LOGIN_DAY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_ID_FIELD_NUMBER: _ClassVar[int]
    level: int
    login_day: int
    language_id: int
    def __init__(self, level: _Optional[int] = ..., login_day: _Optional[int] = ..., language_id: _Optional[int] = ...) -> None: ...
