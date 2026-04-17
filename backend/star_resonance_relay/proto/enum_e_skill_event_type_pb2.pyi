from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ESkillEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SkillEventNone: _ClassVar[ESkillEventType]
    SkillEventTimer: _ClassVar[ESkillEventType]
    SkillEventHit: _ClassVar[ESkillEventType]
    SkillEventBullet: _ClassVar[ESkillEventType]
    SkillEventMotion: _ClassVar[ESkillEventType]
    SkillEventRotation: _ClassVar[ESkillEventType]
    SkillEventFakeBullet: _ClassVar[ESkillEventType]
    SkillEventThrowMove: _ClassVar[ESkillEventType]
    SkillEventBulletHit: _ClassVar[ESkillEventType]
    SkillEventSkillBegin: _ClassVar[ESkillEventType]
    SkillEventSingingEnd: _ClassVar[ESkillEventType]
    SkillEventAccumulateEnd: _ClassVar[ESkillEventType]
    SkillEventSkillEnd: _ClassVar[ESkillEventType]
    SkillEventStageBegin: _ClassVar[ESkillEventType]
SkillEventNone: ESkillEventType
SkillEventTimer: ESkillEventType
SkillEventHit: ESkillEventType
SkillEventBullet: ESkillEventType
SkillEventMotion: ESkillEventType
SkillEventRotation: ESkillEventType
SkillEventFakeBullet: ESkillEventType
SkillEventThrowMove: ESkillEventType
SkillEventBulletHit: ESkillEventType
SkillEventSkillBegin: ESkillEventType
SkillEventSingingEnd: ESkillEventType
SkillEventAccumulateEnd: ESkillEventType
SkillEventSkillEnd: ESkillEventType
SkillEventStageBegin: ESkillEventType
