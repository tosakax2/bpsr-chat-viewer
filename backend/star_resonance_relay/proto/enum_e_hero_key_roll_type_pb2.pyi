from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EHeroKeyRollType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HeroKeyRollTypeNull: _ClassVar[EHeroKeyRollType]
    HeroKeyRollTypeGiveup: _ClassVar[EHeroKeyRollType]
    HeroKeyRollTypeRoll: _ClassVar[EHeroKeyRollType]
    HeroKeyRollTypeGet: _ClassVar[EHeroKeyRollType]
    HeroKeyRollTypeRollGet: _ClassVar[EHeroKeyRollType]
    HeroKeyRollTypeCountFull: _ClassVar[EHeroKeyRollType]
HeroKeyRollTypeNull: EHeroKeyRollType
HeroKeyRollTypeGiveup: EHeroKeyRollType
HeroKeyRollTypeRoll: EHeroKeyRollType
HeroKeyRollTypeGet: EHeroKeyRollType
HeroKeyRollTypeRollGet: EHeroKeyRollType
HeroKeyRollTypeCountFull: EHeroKeyRollType
