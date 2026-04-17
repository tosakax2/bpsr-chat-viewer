from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyCommunityIntroductionChangeRequest(_message.Message):
    __slots__ = ("introduction",)
    INTRODUCTION_FIELD_NUMBER: _ClassVar[int]
    introduction: str
    def __init__(self, introduction: _Optional[str] = ...) -> None: ...
