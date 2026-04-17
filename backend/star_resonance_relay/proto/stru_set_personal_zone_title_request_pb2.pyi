from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetPersonalZoneTitleRequest(_message.Message):
    __slots__ = ("title_id",)
    TITLE_ID_FIELD_NUMBER: _ClassVar[int]
    title_id: int
    def __init__(self, title_id: _Optional[int] = ...) -> None: ...
