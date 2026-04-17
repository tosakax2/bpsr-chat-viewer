from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ESkillCostType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SkillCostRes: _ClassVar[ESkillCostType]
    SkillCostAttr: _ClassVar[ESkillCostType]
    SkillCostBuff: _ClassVar[ESkillCostType]
    SkillCostProp: _ClassVar[ESkillCostType]
    SkillCostResPercent: _ClassVar[ESkillCostType]
SkillCostRes: ESkillCostType
SkillCostAttr: ESkillCostType
SkillCostBuff: ESkillCostType
SkillCostProp: ESkillCostType
SkillCostResPercent: ESkillCostType
