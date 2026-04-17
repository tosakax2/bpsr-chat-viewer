from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EMonsterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Monster: _ClassVar[EMonsterType]
    Elite: _ClassVar[EMonsterType]
    Boss: _ClassVar[EMonsterType]
Monster: EMonsterType
Elite: EMonsterType
Boss: EMonsterType
