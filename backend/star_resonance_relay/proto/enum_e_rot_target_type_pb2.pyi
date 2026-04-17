from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ERotTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RotTargetDefault: _ClassVar[ERotTargetType]
    RotTargetTargetRot: _ClassVar[ERotTargetType]
    RotTargetTarget: _ClassVar[ERotTargetType]
    RotTargetInputDir: _ClassVar[ERotTargetType]
    RotTargetReverseInputDir: _ClassVar[ERotTargetType]
RotTargetDefault: ERotTargetType
RotTargetTargetRot: ERotTargetType
RotTargetTarget: ERotTargetType
RotTargetInputDir: ERotTargetType
RotTargetReverseInputDir: ERotTargetType
