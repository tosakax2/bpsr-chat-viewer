import stru_community_authority_info_pb2 as _stru_community_authority_info_pb2
import stru_community_player_info_pb2 as _stru_community_player_info_pb2
import stru_homeland_decoration_info_pb2 as _stru_homeland_decoration_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomelandVisitInfo(_message.Message):
    __slots__ = ("homeland_id", "level", "cleanliness", "house_owner_char_id", "name", "introduction", "outer_empty_land", "inner_empty_land", "flowers_num", "furniture_state", "cohabitant", "authority_info", "outer_decoration_info", "inner_decoration_info", "unlocked_areas", "housing_type", "field_id", "is_homeland_friend")
    class FurnitureStateEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class CohabitantEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_community_player_info_pb2.CommunityPlayerInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_community_player_info_pb2.CommunityPlayerInfo, _Mapping]] = ...) -> None: ...
    HOMELAND_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CLEANLINESS_FIELD_NUMBER: _ClassVar[int]
    HOUSE_OWNER_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INTRODUCTION_FIELD_NUMBER: _ClassVar[int]
    OUTER_EMPTY_LAND_FIELD_NUMBER: _ClassVar[int]
    INNER_EMPTY_LAND_FIELD_NUMBER: _ClassVar[int]
    FLOWERS_NUM_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_STATE_FIELD_NUMBER: _ClassVar[int]
    COHABITANT_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_INFO_FIELD_NUMBER: _ClassVar[int]
    OUTER_DECORATION_INFO_FIELD_NUMBER: _ClassVar[int]
    INNER_DECORATION_INFO_FIELD_NUMBER: _ClassVar[int]
    UNLOCKED_AREAS_FIELD_NUMBER: _ClassVar[int]
    HOUSING_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    IS_HOMELAND_FRIEND_FIELD_NUMBER: _ClassVar[int]
    homeland_id: int
    level: int
    cleanliness: int
    house_owner_char_id: int
    name: str
    introduction: str
    outer_empty_land: int
    inner_empty_land: int
    flowers_num: int
    furniture_state: _containers.ScalarMap[int, int]
    cohabitant: _containers.MessageMap[int, _stru_community_player_info_pb2.CommunityPlayerInfo]
    authority_info: _stru_community_authority_info_pb2.CommunityAuthorityInfo
    outer_decoration_info: _stru_homeland_decoration_info_pb2.HomelandDecorationInfo
    inner_decoration_info: _stru_homeland_decoration_info_pb2.HomelandDecorationInfo
    unlocked_areas: _containers.RepeatedScalarFieldContainer[int]
    housing_type: int
    field_id: int
    is_homeland_friend: bool
    def __init__(self, homeland_id: _Optional[int] = ..., level: _Optional[int] = ..., cleanliness: _Optional[int] = ..., house_owner_char_id: _Optional[int] = ..., name: _Optional[str] = ..., introduction: _Optional[str] = ..., outer_empty_land: _Optional[int] = ..., inner_empty_land: _Optional[int] = ..., flowers_num: _Optional[int] = ..., furniture_state: _Optional[_Mapping[int, int]] = ..., cohabitant: _Optional[_Mapping[int, _stru_community_player_info_pb2.CommunityPlayerInfo]] = ..., authority_info: _Optional[_Union[_stru_community_authority_info_pb2.CommunityAuthorityInfo, _Mapping]] = ..., outer_decoration_info: _Optional[_Union[_stru_homeland_decoration_info_pb2.HomelandDecorationInfo, _Mapping]] = ..., inner_decoration_info: _Optional[_Union[_stru_homeland_decoration_info_pb2.HomelandDecorationInfo, _Mapping]] = ..., unlocked_areas: _Optional[_Iterable[int]] = ..., housing_type: _Optional[int] = ..., field_id: _Optional[int] = ..., is_homeland_friend: bool = ...) -> None: ...
