from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EAffixEffectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AffixEffectAll: _ClassVar[EAffixEffectType]
    AffixEffectGain: _ClassVar[EAffixEffectType]
    AffixEffectNegative: _ClassVar[EAffixEffectType]
    AffixEffectHarmonize: _ClassVar[EAffixEffectType]
AffixEffectAll: EAffixEffectType
AffixEffectGain: EAffixEffectType
AffixEffectNegative: EAffixEffectType
AffixEffectHarmonize: EAffixEffectType
