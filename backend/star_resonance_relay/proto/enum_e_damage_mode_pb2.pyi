from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EDamageMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DamageNormal: _ClassVar[EDamageMode]
    DamagePhysical: _ClassVar[EDamageMode]
    DamageMagical: _ClassVar[EDamageMode]
DamageNormal: EDamageMode
DamagePhysical: EDamageMode
DamageMagical: EDamageMode
