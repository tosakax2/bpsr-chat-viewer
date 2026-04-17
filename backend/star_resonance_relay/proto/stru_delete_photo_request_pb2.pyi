from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeletePhotoRequest(_message.Message):
    __slots__ = ("photo_id",)
    PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
    photo_id: int
    def __init__(self, photo_id: _Optional[int] = ...) -> None: ...
