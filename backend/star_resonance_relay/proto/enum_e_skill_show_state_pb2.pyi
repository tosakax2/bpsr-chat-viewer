from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ESkillShowState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ESkillShowNone: _ClassVar[ESkillShowState]
    ESkillEnableInputMove: _ClassVar[ESkillShowState]
    ESkillAimState: _ClassVar[ESkillShowState]
    ESkillAimCameraDir: _ClassVar[ESkillShowState]
    ESkillAimTarget: _ClassVar[ESkillShowState]
ESkillShowNone: ESkillShowState
ESkillEnableInputMove: ESkillShowState
ESkillAimState: ESkillShowState
ESkillAimCameraDir: ESkillShowState
ESkillAimTarget: ESkillShowState
