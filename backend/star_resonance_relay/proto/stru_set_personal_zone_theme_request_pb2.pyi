from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetPersonalZoneThemeRequest(_message.Message):
    __slots__ = ("theme_id",)
    THEME_ID_FIELD_NUMBER: _ClassVar[int]
    theme_id: int
    def __init__(self, theme_id: _Optional[int] = ...) -> None: ...
