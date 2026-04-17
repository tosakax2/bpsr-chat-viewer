from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProfessionSkillInfo(_message.Message):
    __slots__ = ("skill_id", "level", "replace_skill_ids", "remodel_level", "cur_skill_skin", "active_skill_skins")
    class ActiveSkillSkinsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    REPLACE_SKILL_IDS_FIELD_NUMBER: _ClassVar[int]
    REMODEL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CUR_SKILL_SKIN_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_SKILL_SKINS_FIELD_NUMBER: _ClassVar[int]
    skill_id: int
    level: int
    replace_skill_ids: _containers.RepeatedScalarFieldContainer[int]
    remodel_level: int
    cur_skill_skin: int
    active_skill_skins: _containers.ScalarMap[int, bool]
    def __init__(self, skill_id: _Optional[int] = ..., level: _Optional[int] = ..., replace_skill_ids: _Optional[_Iterable[int]] = ..., remodel_level: _Optional[int] = ..., cur_skill_skin: _Optional[int] = ..., active_skill_skins: _Optional[_Mapping[int, bool]] = ...) -> None: ...
