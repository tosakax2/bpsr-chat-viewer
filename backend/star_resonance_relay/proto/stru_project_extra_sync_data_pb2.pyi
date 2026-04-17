import stru_profession_talent_info_pb2 as _stru_profession_talent_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProjectExtraSyncData(_message.Message):
    __slots__ = ("current_talent_id_list", "current_skill_id_list")
    class CurrentSkillIdListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    CURRENT_TALENT_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SKILL_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    current_talent_id_list: _stru_profession_talent_info_pb2.ProfessionTalentInfo
    current_skill_id_list: _containers.ScalarMap[int, int]
    def __init__(self, current_talent_id_list: _Optional[_Union[_stru_profession_talent_info_pb2.ProfessionTalentInfo, _Mapping]] = ..., current_skill_id_list: _Optional[_Mapping[int, int]] = ...) -> None: ...
