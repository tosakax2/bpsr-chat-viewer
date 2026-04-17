from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetFaceUpTokenRequest(_message.Message):
    __slots__ = ("file_suffix",)
    FILE_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    file_suffix: str
    def __init__(self, file_suffix: _Optional[str] = ...) -> None: ...
