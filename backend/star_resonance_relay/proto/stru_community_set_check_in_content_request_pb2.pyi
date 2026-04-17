from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CommunitySetCheckInContentRequest(_message.Message):
    __slots__ = ("check_in_content",)
    CHECK_IN_CONTENT_FIELD_NUMBER: _ClassVar[int]
    check_in_content: str
    def __init__(self, check_in_content: _Optional[str] = ...) -> None: ...
