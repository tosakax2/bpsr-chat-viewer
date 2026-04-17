from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyLeaderApplyListSizeRequest(_message.Message):
    __slots__ = ("v_size",)
    V_SIZE_FIELD_NUMBER: _ClassVar[int]
    v_size: int
    def __init__(self, v_size: _Optional[int] = ...) -> None: ...
