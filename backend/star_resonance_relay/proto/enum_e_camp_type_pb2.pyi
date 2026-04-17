from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ECampType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CampHuman: _ClassVar[ECampType]
    CampMonster: _ClassVar[ECampType]
    CampNeutral: _ClassVar[ECampType]
    CampUnbreakable: _ClassVar[ECampType]
CampHuman: ECampType
CampMonster: ECampType
CampNeutral: ECampType
CampUnbreakable: ECampType
