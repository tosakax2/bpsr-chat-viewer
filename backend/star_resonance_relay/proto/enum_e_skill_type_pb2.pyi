from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ESkillType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SkillNormal: _ClassVar[ESkillType]
    SkillCommon: _ClassVar[ESkillType]
    SkillContinuous: _ClassVar[ESkillType]
    SkillSwitch: _ClassVar[ESkillType]
    SkillCharge: _ClassVar[ESkillType]
    SkillBenediction: _ClassVar[ESkillType]
    SkillSceneMark: _ClassVar[ESkillType]
SkillNormal: ESkillType
SkillCommon: ESkillType
SkillContinuous: ESkillType
SkillSwitch: ESkillType
SkillCharge: ESkillType
SkillBenediction: ESkillType
SkillSceneMark: ESkillType
