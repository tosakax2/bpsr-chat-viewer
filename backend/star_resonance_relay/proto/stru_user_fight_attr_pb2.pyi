import stru_skill_c_d_info_pb2 as _stru_skill_c_d_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserFightAttr(_message.Message):
    __slots__ = ("cur_hp", "max_hp", "origin_energy", "resource_ids", "resources", "is_dead", "dead_time", "revive_id", "cd_info")
    CUR_HP_FIELD_NUMBER: _ClassVar[int]
    MAX_HP_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_ENERGY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_IDS_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    IS_DEAD_FIELD_NUMBER: _ClassVar[int]
    DEAD_TIME_FIELD_NUMBER: _ClassVar[int]
    REVIVE_ID_FIELD_NUMBER: _ClassVar[int]
    CD_INFO_FIELD_NUMBER: _ClassVar[int]
    cur_hp: int
    max_hp: int
    origin_energy: float
    resource_ids: _containers.RepeatedScalarFieldContainer[int]
    resources: _containers.RepeatedScalarFieldContainer[int]
    is_dead: int
    dead_time: int
    revive_id: int
    cd_info: _containers.RepeatedCompositeFieldContainer[_stru_skill_c_d_info_pb2.SkillCDInfo]
    def __init__(self, cur_hp: _Optional[int] = ..., max_hp: _Optional[int] = ..., origin_energy: _Optional[float] = ..., resource_ids: _Optional[_Iterable[int]] = ..., resources: _Optional[_Iterable[int]] = ..., is_dead: _Optional[int] = ..., dead_time: _Optional[int] = ..., revive_id: _Optional[int] = ..., cd_info: _Optional[_Iterable[_Union[_stru_skill_c_d_info_pb2.SkillCDInfo, _Mapping]]] = ...) -> None: ...
