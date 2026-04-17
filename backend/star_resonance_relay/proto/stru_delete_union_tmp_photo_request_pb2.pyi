from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteUnionTmpPhotoRequest(_message.Message):
    __slots__ = ("union_id", "photo_id")
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    photo_id: int
    def __init__(self, union_id: _Optional[int] = ..., photo_id: _Optional[int] = ...) -> None: ...
