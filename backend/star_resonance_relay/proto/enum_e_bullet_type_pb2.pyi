from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EBulletType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BulletTypeServer: _ClassVar[EBulletType]
    BulletTypeFake: _ClassVar[EBulletType]
    BulletTypeClient: _ClassVar[EBulletType]
BulletTypeServer: EBulletType
BulletTypeFake: EBulletType
BulletTypeClient: EBulletType
