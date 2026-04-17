from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EditUnionAlbumNameRequest(_message.Message):
    __slots__ = ("union_id", "album_id", "name")
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    ALBUM_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    album_id: int
    name: str
    def __init__(self, union_id: _Optional[int] = ..., album_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
