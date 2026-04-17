from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EBulletMotionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BulletMotionNormal: _ClassVar[EBulletMotionType]
    BulletMotionLinear: _ClassVar[EBulletMotionType]
    BulletMotionBezier: _ClassVar[EBulletMotionType]
    BulletMotionFollow: _ClassVar[EBulletMotionType]
    BulletMotionSurround: _ClassVar[EBulletMotionType]
BulletMotionNormal: EBulletMotionType
BulletMotionLinear: EBulletMotionType
BulletMotionBezier: EBulletMotionType
BulletMotionFollow: EBulletMotionType
BulletMotionSurround: EBulletMotionType
