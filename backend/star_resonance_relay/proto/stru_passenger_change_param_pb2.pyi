from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PassengerChangeParam(_message.Message):
    __slots__ = ("IsAddPassenger", "AddOrRemoveUuid")
    ISADDPASSENGER_FIELD_NUMBER: _ClassVar[int]
    ADDORREMOVEUUID_FIELD_NUMBER: _ClassVar[int]
    IsAddPassenger: bool
    AddOrRemoveUuid: int
    def __init__(self, IsAddPassenger: bool = ..., AddOrRemoveUuid: _Optional[int] = ...) -> None: ...
