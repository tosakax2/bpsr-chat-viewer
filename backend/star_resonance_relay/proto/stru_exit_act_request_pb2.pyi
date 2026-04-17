from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExitActRequest(_message.Message):
    __slots__ = ("act_id",)
    ACT_ID_FIELD_NUMBER: _ClassVar[int]
    act_id: int
    def __init__(self, act_id: _Optional[int] = ...) -> None: ...
