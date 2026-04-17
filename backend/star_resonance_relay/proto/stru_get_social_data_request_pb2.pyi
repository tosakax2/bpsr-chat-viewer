from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetSocialDataRequest(_message.Message):
    __slots__ = ("char_id", "mask")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    mask: int
    def __init__(self, char_id: _Optional[int] = ..., mask: _Optional[int] = ...) -> None: ...
