from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ECollideType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CollideSphere: _ClassVar[ECollideType]
    CollidePlane: _ClassVar[ECollideType]
    CollideCylinder: _ClassVar[ECollideType]
    CollideCube: _ClassVar[ECollideType]
CollideSphere: ECollideType
CollidePlane: ECollideType
CollideCylinder: ECollideType
CollideCube: ECollideType
