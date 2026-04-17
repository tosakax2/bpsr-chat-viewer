import stru_profession_skill_info_pb2 as _stru_profession_skill_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DutyInfo(_message.Message):
    __slots__ = ("duty_skill_info_map", "duty_skill_slot_info_map")
    class DutySkillInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_profession_skill_info_pb2.ProfessionSkillInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_profession_skill_info_pb2.ProfessionSkillInfo, _Mapping]] = ...) -> None: ...
    class DutySkillSlotInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    DUTY_SKILL_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    DUTY_SKILL_SLOT_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    duty_skill_info_map: _containers.MessageMap[int, _stru_profession_skill_info_pb2.ProfessionSkillInfo]
    duty_skill_slot_info_map: _containers.ScalarMap[int, int]
    def __init__(self, duty_skill_info_map: _Optional[_Mapping[int, _stru_profession_skill_info_pb2.ProfessionSkillInfo]] = ..., duty_skill_slot_info_map: _Optional[_Mapping[int, int]] = ...) -> None: ...
