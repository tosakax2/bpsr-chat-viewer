from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PassengerInfo(_message.Message):
    __slots__ = ("seat_num", "uuid")
    SEAT_NUM_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    seat_num: int
    uuid: int
    def __init__(self, seat_num: _Optional[int] = ..., uuid: _Optional[int] = ...) -> None: ...
