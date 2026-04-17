from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EDamageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Normal: _ClassVar[EDamageType]
    Miss: _ClassVar[EDamageType]
    Heal: _ClassVar[EDamageType]
    Immune: _ClassVar[EDamageType]
    Fall: _ClassVar[EDamageType]
    Absorbed: _ClassVar[EDamageType]
Normal: EDamageType
Miss: EDamageType
Heal: EDamageType
Immune: EDamageType
Fall: EDamageType
Absorbed: EDamageType
