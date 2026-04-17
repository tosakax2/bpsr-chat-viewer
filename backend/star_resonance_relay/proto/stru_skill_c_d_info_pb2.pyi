from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SkillCDInfo(_message.Message):
    __slots__ = ("skill_level_id", "skill_begin_time", "duration", "skill_cd_type", "profession_hold_begin_time", "charge_count", "valid_cd_time", "sub_cd_ratio", "sub_cd_fixed", "accelerate_cd_ratio")
    SKILL_LEVEL_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    SKILL_CD_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROFESSION_HOLD_BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    CHARGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VALID_CD_TIME_FIELD_NUMBER: _ClassVar[int]
    SUB_CD_RATIO_FIELD_NUMBER: _ClassVar[int]
    SUB_CD_FIXED_FIELD_NUMBER: _ClassVar[int]
    ACCELERATE_CD_RATIO_FIELD_NUMBER: _ClassVar[int]
    skill_level_id: int
    skill_begin_time: int
    duration: int
    skill_cd_type: int
    profession_hold_begin_time: int
    charge_count: int
    valid_cd_time: int
    sub_cd_ratio: int
    sub_cd_fixed: int
    accelerate_cd_ratio: int
    def __init__(self, skill_level_id: _Optional[int] = ..., skill_begin_time: _Optional[int] = ..., duration: _Optional[int] = ..., skill_cd_type: _Optional[int] = ..., profession_hold_begin_time: _Optional[int] = ..., charge_count: _Optional[int] = ..., valid_cd_time: _Optional[int] = ..., sub_cd_ratio: _Optional[int] = ..., sub_cd_fixed: _Optional[int] = ..., accelerate_cd_ratio: _Optional[int] = ...) -> None: ...
