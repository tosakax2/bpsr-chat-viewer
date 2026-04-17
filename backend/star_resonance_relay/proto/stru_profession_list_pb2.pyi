import stru_profession_info_pb2 as _stru_profession_info_pb2
import stru_profession_skill_info_pb2 as _stru_profession_skill_info_pb2
import stru_profession_talent_info_pb2 as _stru_profession_talent_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProfessionList(_message.Message):
    __slots__ = ("cur_profession_id", "cur_assist_professions", "profession_list", "aoyi_skill_info_map", "total_talent_points", "total_talent_reset_count", "talent_list", "reset_profession_list_flag", "total_attack_mark", "total_guard_mark", "total_heal_mark", "reset_talent_mark_item_flag", "reset_talent_mark_item_pop_up_notice")
    class ProfessionListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_profession_info_pb2.ProfessionInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_profession_info_pb2.ProfessionInfo, _Mapping]] = ...) -> None: ...
    class AoyiSkillInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_profession_skill_info_pb2.ProfessionSkillInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_profession_skill_info_pb2.ProfessionSkillInfo, _Mapping]] = ...) -> None: ...
    class TalentListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_profession_talent_info_pb2.ProfessionTalentInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_profession_talent_info_pb2.ProfessionTalentInfo, _Mapping]] = ...) -> None: ...
    CUR_PROFESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CUR_ASSIST_PROFESSIONS_FIELD_NUMBER: _ClassVar[int]
    PROFESSION_LIST_FIELD_NUMBER: _ClassVar[int]
    AOYI_SKILL_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TALENT_POINTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TALENT_RESET_COUNT_FIELD_NUMBER: _ClassVar[int]
    TALENT_LIST_FIELD_NUMBER: _ClassVar[int]
    RESET_PROFESSION_LIST_FLAG_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ATTACK_MARK_FIELD_NUMBER: _ClassVar[int]
    TOTAL_GUARD_MARK_FIELD_NUMBER: _ClassVar[int]
    TOTAL_HEAL_MARK_FIELD_NUMBER: _ClassVar[int]
    RESET_TALENT_MARK_ITEM_FLAG_FIELD_NUMBER: _ClassVar[int]
    RESET_TALENT_MARK_ITEM_POP_UP_NOTICE_FIELD_NUMBER: _ClassVar[int]
    cur_profession_id: int
    cur_assist_professions: _containers.RepeatedScalarFieldContainer[int]
    profession_list: _containers.MessageMap[int, _stru_profession_info_pb2.ProfessionInfo]
    aoyi_skill_info_map: _containers.MessageMap[int, _stru_profession_skill_info_pb2.ProfessionSkillInfo]
    total_talent_points: int
    total_talent_reset_count: int
    talent_list: _containers.MessageMap[int, _stru_profession_talent_info_pb2.ProfessionTalentInfo]
    reset_profession_list_flag: int
    total_attack_mark: int
    total_guard_mark: int
    total_heal_mark: int
    reset_talent_mark_item_flag: int
    reset_talent_mark_item_pop_up_notice: int
    def __init__(self, cur_profession_id: _Optional[int] = ..., cur_assist_professions: _Optional[_Iterable[int]] = ..., profession_list: _Optional[_Mapping[int, _stru_profession_info_pb2.ProfessionInfo]] = ..., aoyi_skill_info_map: _Optional[_Mapping[int, _stru_profession_skill_info_pb2.ProfessionSkillInfo]] = ..., total_talent_points: _Optional[int] = ..., total_talent_reset_count: _Optional[int] = ..., talent_list: _Optional[_Mapping[int, _stru_profession_talent_info_pb2.ProfessionTalentInfo]] = ..., reset_profession_list_flag: _Optional[int] = ..., total_attack_mark: _Optional[int] = ..., total_guard_mark: _Optional[int] = ..., total_heal_mark: _Optional[int] = ..., reset_talent_mark_item_flag: _Optional[int] = ..., reset_talent_mark_item_pop_up_notice: _Optional[int] = ...) -> None: ...
