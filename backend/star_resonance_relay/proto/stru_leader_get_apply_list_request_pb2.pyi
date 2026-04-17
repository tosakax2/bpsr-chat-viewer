from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LeaderGetApplyListRequest(_message.Message):
    __slots__ = ("is_refresh",)
    IS_REFRESH_FIELD_NUMBER: _ClassVar[int]
    is_refresh: bool
    def __init__(self, is_refresh: bool = ...) -> None: ...
