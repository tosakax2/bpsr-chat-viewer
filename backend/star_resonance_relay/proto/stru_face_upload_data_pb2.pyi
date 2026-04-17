from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FaceUploadData(_message.Message):
    __slots__ = ("short_guid", "file_suffix")
    SHORT_GUID_FIELD_NUMBER: _ClassVar[int]
    FILE_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    short_guid: str
    file_suffix: str
    def __init__(self, short_guid: _Optional[str] = ..., file_suffix: _Optional[str] = ...) -> None: ...
