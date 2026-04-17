from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EApplyRideResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ApplyRideResultNone: _ClassVar[EApplyRideResult]
    ApplyRideResultAgree: _ClassVar[EApplyRideResult]
    ApplyRideResultRefuse: _ClassVar[EApplyRideResult]
    ApplyRideResultTimeOut: _ClassVar[EApplyRideResult]
ApplyRideResultNone: EApplyRideResult
ApplyRideResultAgree: EApplyRideResult
ApplyRideResultRefuse: EApplyRideResult
ApplyRideResultTimeOut: EApplyRideResult
