from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyCommunityApplyUpdateRequest(_message.Message):
    __slots__ = ("is_update",)
    IS_UPDATE_FIELD_NUMBER: _ClassVar[int]
    is_update: bool
    def __init__(self, is_update: bool = ...) -> None: ...
