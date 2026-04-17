from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DriverApplyRideParam(_message.Message):
    __slots__ = ("apply_id", "apply_name")
    APPLY_ID_FIELD_NUMBER: _ClassVar[int]
    APPLY_NAME_FIELD_NUMBER: _ClassVar[int]
    apply_id: int
    apply_name: str
    def __init__(self, apply_id: _Optional[int] = ..., apply_name: _Optional[str] = ...) -> None: ...
