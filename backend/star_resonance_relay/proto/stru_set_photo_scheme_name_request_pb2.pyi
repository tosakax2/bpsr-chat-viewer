from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetPhotoSchemeNameRequest(_message.Message):
    __slots__ = ("scheme_id", "scheme_name")
    SCHEME_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEME_NAME_FIELD_NUMBER: _ClassVar[int]
    scheme_id: int
    scheme_name: str
    def __init__(self, scheme_id: _Optional[int] = ..., scheme_name: _Optional[str] = ...) -> None: ...
