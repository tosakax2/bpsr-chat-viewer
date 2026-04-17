from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReplyJoinActivityRequest(_message.Message):
    __slots__ = ("is_agree",)
    IS_AGREE_FIELD_NUMBER: _ClassVar[int]
    is_agree: bool
    def __init__(self, is_agree: bool = ...) -> None: ...
