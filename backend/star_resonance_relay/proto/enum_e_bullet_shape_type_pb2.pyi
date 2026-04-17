from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EBulletShapeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BulletShapeBall: _ClassVar[EBulletShapeType]
    BulletShapeRing: _ClassVar[EBulletShapeType]
    BulletShapeCube: _ClassVar[EBulletShapeType]
    BulletShapeCylinder: _ClassVar[EBulletShapeType]
    BulletShapeBallRay: _ClassVar[EBulletShapeType]
    BulletShapePoint: _ClassVar[EBulletShapeType]
BulletShapeBall: EBulletShapeType
BulletShapeRing: EBulletShapeType
BulletShapeCube: EBulletShapeType
BulletShapeCylinder: EBulletShapeType
BulletShapeBallRay: EBulletShapeType
BulletShapePoint: EBulletShapeType
