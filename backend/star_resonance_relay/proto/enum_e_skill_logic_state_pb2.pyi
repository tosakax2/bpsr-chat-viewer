from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ESkillLogicState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ESkillLogicNone: _ClassVar[ESkillLogicState]
    ESkillCombo: _ClassVar[ESkillLogicState]
    ESkillAfterCache: _ClassVar[ESkillLogicState]
    ESkillAfter: _ClassVar[ESkillLogicState]
    ESkillHang: _ClassVar[ESkillLogicState]
    ESkillSpecialBreakOff: _ClassVar[ESkillLogicState]
    ERushCanInterrupt: _ClassVar[ESkillLogicState]
    EChangeProfession: _ClassVar[ESkillLogicState]
ESkillLogicNone: ESkillLogicState
ESkillCombo: ESkillLogicState
ESkillAfterCache: ESkillLogicState
ESkillAfter: ESkillLogicState
ESkillHang: ESkillLogicState
ESkillSpecialBreakOff: ESkillLogicState
ERushCanInterrupt: ESkillLogicState
EChangeProfession: ESkillLogicState
