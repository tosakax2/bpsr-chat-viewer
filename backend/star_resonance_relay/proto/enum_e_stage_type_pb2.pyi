from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EStageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENormal: _ClassVar[EStageType]
    ESinging: _ClassVar[EStageType]
    EEnergy: _ClassVar[EStageType]
    EAim: _ClassVar[EStageType]
    EAimShooting: _ClassVar[EStageType]
    EBossRotInplace: _ClassVar[EStageType]
    EBossRotJump: _ClassVar[EStageType]
    EOnGrounded: _ClassVar[EStageType]
    EGuideNormal: _ClassVar[EStageType]
    EGuideTimeUnChanged: _ClassVar[EStageType]
ENormal: EStageType
ESinging: EStageType
EEnergy: EStageType
EAim: EStageType
EAimShooting: EStageType
EBossRotInplace: EStageType
EBossRotJump: EStageType
EOnGrounded: EStageType
EGuideNormal: EStageType
EGuideTimeUnChanged: EStageType
