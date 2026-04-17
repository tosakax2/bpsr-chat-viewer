import stru_community_player_info_pb2 as _stru_community_player_info_pb2
import stru_home_land_clutter_generation_record_pb2 as _stru_home_land_clutter_generation_record_pb2
import stru_home_land_clutter_info_pb2 as _stru_home_land_clutter_info_pb2
import stru_homeland_decoration_info_pb2 as _stru_homeland_decoration_info_pb2
import stru_structure_pb2 as _stru_structure_pb2
import stru_structure_group_info_pb2 as _stru_structure_group_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomelandInfo(_message.Message):
    __slots__ = ("owner_char_id", "homeland_id", "field_id", "name", "level", "exp", "cleanliness", "lastsubtractcleanlinesstime", "home_land_clutter", "home_land_clutter_generation_record", "structures", "groups", "cohabitant", "outer_decoration_info", "inner_decoration_info", "unlocked_areas", "housing_type")
    class StructuresEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_structure_pb2.Structure
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_structure_pb2.Structure, _Mapping]] = ...) -> None: ...
    class GroupsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_structure_group_info_pb2.StructureGroupInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_structure_group_info_pb2.StructureGroupInfo, _Mapping]] = ...) -> None: ...
    class CohabitantEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_community_player_info_pb2.CommunityPlayerInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_community_player_info_pb2.CommunityPlayerInfo, _Mapping]] = ...) -> None: ...
    OWNER_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    HOMELAND_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    CLEANLINESS_FIELD_NUMBER: _ClassVar[int]
    LASTSUBTRACTCLEANLINESSTIME_FIELD_NUMBER: _ClassVar[int]
    HOME_LAND_CLUTTER_FIELD_NUMBER: _ClassVar[int]
    HOME_LAND_CLUTTER_GENERATION_RECORD_FIELD_NUMBER: _ClassVar[int]
    STRUCTURES_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    COHABITANT_FIELD_NUMBER: _ClassVar[int]
    OUTER_DECORATION_INFO_FIELD_NUMBER: _ClassVar[int]
    INNER_DECORATION_INFO_FIELD_NUMBER: _ClassVar[int]
    UNLOCKED_AREAS_FIELD_NUMBER: _ClassVar[int]
    HOUSING_TYPE_FIELD_NUMBER: _ClassVar[int]
    owner_char_id: int
    homeland_id: int
    field_id: int
    name: str
    level: int
    exp: int
    cleanliness: int
    lastsubtractcleanlinesstime: int
    home_land_clutter: _stru_home_land_clutter_info_pb2.HomeLandClutterInfo
    home_land_clutter_generation_record: _stru_home_land_clutter_generation_record_pb2.HomeLandClutterGenerationRecord
    structures: _containers.MessageMap[int, _stru_structure_pb2.Structure]
    groups: _containers.MessageMap[int, _stru_structure_group_info_pb2.StructureGroupInfo]
    cohabitant: _containers.MessageMap[int, _stru_community_player_info_pb2.CommunityPlayerInfo]
    outer_decoration_info: _stru_homeland_decoration_info_pb2.HomelandDecorationInfo
    inner_decoration_info: _stru_homeland_decoration_info_pb2.HomelandDecorationInfo
    unlocked_areas: _containers.RepeatedScalarFieldContainer[int]
    housing_type: int
    def __init__(self, owner_char_id: _Optional[int] = ..., homeland_id: _Optional[int] = ..., field_id: _Optional[int] = ..., name: _Optional[str] = ..., level: _Optional[int] = ..., exp: _Optional[int] = ..., cleanliness: _Optional[int] = ..., lastsubtractcleanlinesstime: _Optional[int] = ..., home_land_clutter: _Optional[_Union[_stru_home_land_clutter_info_pb2.HomeLandClutterInfo, _Mapping]] = ..., home_land_clutter_generation_record: _Optional[_Union[_stru_home_land_clutter_generation_record_pb2.HomeLandClutterGenerationRecord, _Mapping]] = ..., structures: _Optional[_Mapping[int, _stru_structure_pb2.Structure]] = ..., groups: _Optional[_Mapping[int, _stru_structure_group_info_pb2.StructureGroupInfo]] = ..., cohabitant: _Optional[_Mapping[int, _stru_community_player_info_pb2.CommunityPlayerInfo]] = ..., outer_decoration_info: _Optional[_Union[_stru_homeland_decoration_info_pb2.HomelandDecorationInfo, _Mapping]] = ..., inner_decoration_info: _Optional[_Union[_stru_homeland_decoration_info_pb2.HomelandDecorationInfo, _Mapping]] = ..., unlocked_areas: _Optional[_Iterable[int]] = ..., housing_type: _Optional[int] = ...) -> None: ...
