from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PrivateChatTargetTopRequest(_message.Message):
    __slots__ = ("target_id", "set_top")
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    SET_TOP_FIELD_NUMBER: _ClassVar[int]
    target_id: int
    set_top: bool
    def __init__(self, target_id: _Optional[int] = ..., set_top: bool = ...) -> None: ...
