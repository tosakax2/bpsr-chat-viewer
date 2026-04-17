from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ESkillSelectPointType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENouseStrategy: _ClassVar[ESkillSelectPointType]
    EHorizontalRayCast: _ClassVar[ESkillSelectPointType]
    EFittedGroundPoint: _ClassVar[ESkillSelectPointType]
ENouseStrategy: ESkillSelectPointType
EHorizontalRayCast: ESkillSelectPointType
EFittedGroundPoint: ESkillSelectPointType
