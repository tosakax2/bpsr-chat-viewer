from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EditAlbumNameRequest(_message.Message):
    __slots__ = ("album_id", "name")
    ALBUM_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    album_id: int
    name: str
    def __init__(self, album_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
