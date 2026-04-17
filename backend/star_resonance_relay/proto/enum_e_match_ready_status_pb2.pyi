from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EMatchReadyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMatchReadyStatusWait: _ClassVar[EMatchReadyStatus]
    EMatchReadyStatusReady: _ClassVar[EMatchReadyStatus]
    EMatchReadyStatusUnReady: _ClassVar[EMatchReadyStatus]
EMatchReadyStatusWait: EMatchReadyStatus
EMatchReadyStatusReady: EMatchReadyStatus
EMatchReadyStatusUnReady: EMatchReadyStatus
