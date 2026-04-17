from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonTitleInfo(_message.Message):
    __slots__ = ("uuid", "title_id")
    UUID_FIELD_NUMBER: _ClassVar[int]
    TITLE_ID_FIELD_NUMBER: _ClassVar[int]
    uuid: int
    title_id: int
    def __init__(self, uuid: _Optional[int] = ..., title_id: _Optional[int] = ...) -> None: ...
