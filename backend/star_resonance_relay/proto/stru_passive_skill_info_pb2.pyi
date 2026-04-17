from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PassiveSkillInfo(_message.Message):
    __slots__ = ("Uuid", "TargetUuid", "StageBeginTime", "BeginTime", "StagePlayNum", "SkillId", "SkillLevel", "SkillStage")
    UUID_FIELD_NUMBER: _ClassVar[int]
    TARGETUUID_FIELD_NUMBER: _ClassVar[int]
    STAGEBEGINTIME_FIELD_NUMBER: _ClassVar[int]
    BEGINTIME_FIELD_NUMBER: _ClassVar[int]
    STAGEPLAYNUM_FIELD_NUMBER: _ClassVar[int]
    SKILLID_FIELD_NUMBER: _ClassVar[int]
    SKILLLEVEL_FIELD_NUMBER: _ClassVar[int]
    SKILLSTAGE_FIELD_NUMBER: _ClassVar[int]
    Uuid: int
    TargetUuid: int
    StageBeginTime: int
    BeginTime: int
    StagePlayNum: int
    SkillId: int
    SkillLevel: int
    SkillStage: int
    def __init__(self, Uuid: _Optional[int] = ..., TargetUuid: _Optional[int] = ..., StageBeginTime: _Optional[int] = ..., BeginTime: _Optional[int] = ..., StagePlayNum: _Optional[int] = ..., SkillId: _Optional[int] = ..., SkillLevel: _Optional[int] = ..., SkillStage: _Optional[int] = ...) -> None: ...
