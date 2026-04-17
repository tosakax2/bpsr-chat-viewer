from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InviteApplyRideParam(_message.Message):
    __slots__ = ("driver_id", "driver_name")
    DRIVER_ID_FIELD_NUMBER: _ClassVar[int]
    DRIVER_NAME_FIELD_NUMBER: _ClassVar[int]
    driver_id: int
    driver_name: str
    def __init__(self, driver_id: _Optional[int] = ..., driver_name: _Optional[str] = ...) -> None: ...
