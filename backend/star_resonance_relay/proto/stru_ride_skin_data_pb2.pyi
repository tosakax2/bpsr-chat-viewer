from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RideSkinData(_message.Message):
    __slots__ = ("activate_time",)
    ACTIVATE_TIME_FIELD_NUMBER: _ClassVar[int]
    activate_time: int
    def __init__(self, activate_time: _Optional[int] = ...) -> None: ...
