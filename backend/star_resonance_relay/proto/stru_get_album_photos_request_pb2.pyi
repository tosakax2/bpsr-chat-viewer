from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetAlbumPhotosRequest(_message.Message):
    __slots__ = ("char_id", "album_id")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    ALBUM_ID_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    album_id: int
    def __init__(self, char_id: _Optional[int] = ..., album_id: _Optional[int] = ...) -> None: ...
