from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MagneticQueueAppearInfo(_message.Message):
    __slots__ = ("PassengerUuidList", "IsCircle", "PathLength")
    PASSENGERUUIDLIST_FIELD_NUMBER: _ClassVar[int]
    ISCIRCLE_FIELD_NUMBER: _ClassVar[int]
    PATHLENGTH_FIELD_NUMBER: _ClassVar[int]
    PassengerUuidList: _containers.RepeatedScalarFieldContainer[int]
    IsCircle: bool
    PathLength: float
    def __init__(self, PassengerUuidList: _Optional[_Iterable[int]] = ..., IsCircle: bool = ..., PathLength: _Optional[float] = ...) -> None: ...
