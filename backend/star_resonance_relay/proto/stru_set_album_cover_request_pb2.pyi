from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetAlbumCoverRequest(_message.Message):
    __slots__ = ("album_id", "cover_photo_id")
    ALBUM_ID_FIELD_NUMBER: _ClassVar[int]
    COVER_PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    album_id: int
    cover_photo_id: int
    def __init__(self, album_id: _Optional[int] = ..., cover_photo_id: _Optional[int] = ...) -> None: ...
