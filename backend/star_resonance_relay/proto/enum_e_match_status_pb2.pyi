from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EMatchStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMatchStatusNull: _ClassVar[EMatchStatus]
    EMatchStatusMatching: _ClassVar[EMatchStatus]
    EMatchStatusWaitReady: _ClassVar[EMatchStatus]
    EMatchStatusAllReady: _ClassVar[EMatchStatus]
    EMatchStatusSuccess: _ClassVar[EMatchStatus]
EMatchStatusNull: EMatchStatus
EMatchStatusMatching: EMatchStatus
EMatchStatusWaitReady: EMatchStatus
EMatchStatusAllReady: EMatchStatus
EMatchStatusSuccess: EMatchStatus
