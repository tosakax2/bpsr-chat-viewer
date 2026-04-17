from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PhotoOwnerData(_message.Message):
    __slots__ = ("upload_char_id", "expire_time", "show_id", "name")
    UPLOAD_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    SHOW_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    upload_char_id: int
    expire_time: int
    show_id: int
    name: str
    def __init__(self, upload_char_id: _Optional[int] = ..., expire_time: _Optional[int] = ..., show_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
