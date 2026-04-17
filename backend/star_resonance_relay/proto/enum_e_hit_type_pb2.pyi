from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EHitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HitTypeInHand: _ClassVar[EHitType]
    HitTypeOutHand: _ClassVar[EHitType]
HitTypeInHand: EHitType
HitTypeOutHand: EHitType
