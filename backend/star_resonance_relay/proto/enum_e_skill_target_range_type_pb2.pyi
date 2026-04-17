from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ESkillTargetRangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SkillPassive: _ClassVar[ESkillTargetRangeType]
    SkillTarget: _ClassVar[ESkillTargetRangeType]
    SkillDir: _ClassVar[ESkillTargetRangeType]
    SkillPos: _ClassVar[ESkillTargetRangeType]
    SkillSelf: _ClassVar[ESkillTargetRangeType]
SkillPassive: ESkillTargetRangeType
SkillTarget: ESkillTargetRangeType
SkillDir: ESkillTargetRangeType
SkillPos: ESkillTargetRangeType
SkillSelf: ESkillTargetRangeType
