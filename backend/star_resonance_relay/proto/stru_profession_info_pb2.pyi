import stru_profession_skill_info_pb2 as _stru_profession_skill_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProfessionInfo(_message.Message):
    __slots__ = ("profession_id", "level", "experience", "skill_info_map", "active_skill_ids", "slot_skill_info_map", "use_skin_id")
    class SkillInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_profession_skill_info_pb2.ProfessionSkillInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_profession_skill_info_pb2.ProfessionSkillInfo, _Mapping]] = ...) -> None: ...
    class SlotSkillInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PROFESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXPERIENCE_FIELD_NUMBER: _ClassVar[int]
    SKILL_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_SKILL_IDS_FIELD_NUMBER: _ClassVar[int]
    SLOT_SKILL_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    USE_SKIN_ID_FIELD_NUMBER: _ClassVar[int]
    profession_id: int
    level: int
    experience: int
    skill_info_map: _containers.MessageMap[int, _stru_profession_skill_info_pb2.ProfessionSkillInfo]
    active_skill_ids: _containers.RepeatedScalarFieldContainer[int]
    slot_skill_info_map: _containers.ScalarMap[int, int]
    use_skin_id: int
    def __init__(self, profession_id: _Optional[int] = ..., level: _Optional[int] = ..., experience: _Optional[int] = ..., skill_info_map: _Optional[_Mapping[int, _stru_profession_skill_info_pb2.ProfessionSkillInfo]] = ..., active_skill_ids: _Optional[_Iterable[int]] = ..., slot_skill_info_map: _Optional[_Mapping[int, int]] = ..., use_skin_id: _Optional[int] = ...) -> None: ...
