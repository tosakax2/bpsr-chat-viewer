from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EBulletDirectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ESummonerDir: _ClassVar[EBulletDirectionType]
    ETargetPos: _ClassVar[EBulletDirectionType]
    ETargetEnt: _ClassVar[EBulletDirectionType]
ESummonerDir: EBulletDirectionType
ETargetPos: EBulletDirectionType
ETargetEnt: EBulletDirectionType
