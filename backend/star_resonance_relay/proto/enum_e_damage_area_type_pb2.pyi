from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EDamageAreaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DamageNone: _ClassVar[EDamageAreaType]
    DamageCylinder: _ClassVar[EDamageAreaType]
    DamageCube: _ClassVar[EDamageAreaType]
    DamageSector: _ClassVar[EDamageAreaType]
    DamageAnnulus: _ClassVar[EDamageAreaType]
    DamageSphere: _ClassVar[EDamageAreaType]
    DamagePoint: _ClassVar[EDamageAreaType]
DamageNone: EDamageAreaType
DamageCylinder: EDamageAreaType
DamageCube: EDamageAreaType
DamageSector: EDamageAreaType
DamageAnnulus: EDamageAreaType
DamageSphere: EDamageAreaType
DamagePoint: EDamageAreaType
