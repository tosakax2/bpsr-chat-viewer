from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RideData(_message.Message):
    __slots__ = ("ride_id",)
    RIDE_ID_FIELD_NUMBER: _ClassVar[int]
    ride_id: int
    def __init__(self, ride_id: _Optional[int] = ...) -> None: ...
