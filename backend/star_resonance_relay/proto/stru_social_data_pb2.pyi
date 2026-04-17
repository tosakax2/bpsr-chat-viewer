import stru_account_data_pb2 as _stru_account_data_pb2
import stru_avatar_info_pb2 as _stru_avatar_info_pb2
import stru_basic_data_pb2 as _stru_basic_data_pb2
import stru_char_team_pb2 as _stru_char_team_pb2
import stru_community_data_pb2 as _stru_community_data_pb2
import stru_equip_data_pb2 as _stru_equip_data_pb2
import stru_face_data_pb2 as _stru_face_data_pb2
import stru_fashion_data_pb2 as _stru_fashion_data_pb2
import stru_fish_social_data_pb2 as _stru_fish_social_data_pb2
import stru_function_data_pb2 as _stru_function_data_pb2
import stru_master_mode_dungeon_data_pb2 as _stru_master_mode_dungeon_data_pb2
import stru_personal_zone_pb2 as _stru_personal_zone_pb2
import stru_privilege_data_pb2 as _stru_privilege_data_pb2
import stru_profession_data_pb2 as _stru_profession_data_pb2
import stru_scene_data_pb2 as _stru_scene_data_pb2
import stru_season_rank_data_pb2 as _stru_season_rank_data_pb2
import stru_setting_data_pb2 as _stru_setting_data_pb2
import stru_union_data_pb2 as _stru_union_data_pb2
import stru_user_attr_data_pb2 as _stru_user_attr_data_pb2
import stru_warehouse_data_pb2 as _stru_warehouse_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SocialData(_message.Message):
    __slots__ = ("char_id", "account_id", "basic_data", "avatar_info", "face_data", "profession_data", "equip_data", "fashion_data", "setting_data", "scene_data", "user_attr_data", "team_data", "union_data", "account_data", "function_data", "personal_zone", "warehouse", "season_rank", "fish_data", "community_data", "privilege_data", "master_mode_dungeon_data")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    BASIC_DATA_FIELD_NUMBER: _ClassVar[int]
    AVATAR_INFO_FIELD_NUMBER: _ClassVar[int]
    FACE_DATA_FIELD_NUMBER: _ClassVar[int]
    PROFESSION_DATA_FIELD_NUMBER: _ClassVar[int]
    EQUIP_DATA_FIELD_NUMBER: _ClassVar[int]
    FASHION_DATA_FIELD_NUMBER: _ClassVar[int]
    SETTING_DATA_FIELD_NUMBER: _ClassVar[int]
    SCENE_DATA_FIELD_NUMBER: _ClassVar[int]
    USER_ATTR_DATA_FIELD_NUMBER: _ClassVar[int]
    TEAM_DATA_FIELD_NUMBER: _ClassVar[int]
    UNION_DATA_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_DATA_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_DATA_FIELD_NUMBER: _ClassVar[int]
    PERSONAL_ZONE_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    SEASON_RANK_FIELD_NUMBER: _ClassVar[int]
    FISH_DATA_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_DATA_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGE_DATA_FIELD_NUMBER: _ClassVar[int]
    MASTER_MODE_DUNGEON_DATA_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    account_id: str
    basic_data: _stru_basic_data_pb2.BasicData
    avatar_info: _stru_avatar_info_pb2.AvatarInfo
    face_data: _stru_face_data_pb2.FaceData
    profession_data: _stru_profession_data_pb2.ProfessionData
    equip_data: _stru_equip_data_pb2.EquipData
    fashion_data: _stru_fashion_data_pb2.FashionData
    setting_data: _stru_setting_data_pb2.SettingData
    scene_data: _stru_scene_data_pb2.SceneData
    user_attr_data: _stru_user_attr_data_pb2.UserAttrData
    team_data: _stru_char_team_pb2.CharTeam
    union_data: _stru_union_data_pb2.UnionData
    account_data: _stru_account_data_pb2.AccountData
    function_data: _stru_function_data_pb2.FunctionData
    personal_zone: _stru_personal_zone_pb2.PersonalZone
    warehouse: _stru_warehouse_data_pb2.WarehouseData
    season_rank: _stru_season_rank_data_pb2.SeasonRankData
    fish_data: _stru_fish_social_data_pb2.FishSocialData
    community_data: _stru_community_data_pb2.CommunityData
    privilege_data: _stru_privilege_data_pb2.PrivilegeData
    master_mode_dungeon_data: _stru_master_mode_dungeon_data_pb2.MasterModeDungeonData
    def __init__(self, char_id: _Optional[int] = ..., account_id: _Optional[str] = ..., basic_data: _Optional[_Union[_stru_basic_data_pb2.BasicData, _Mapping]] = ..., avatar_info: _Optional[_Union[_stru_avatar_info_pb2.AvatarInfo, _Mapping]] = ..., face_data: _Optional[_Union[_stru_face_data_pb2.FaceData, _Mapping]] = ..., profession_data: _Optional[_Union[_stru_profession_data_pb2.ProfessionData, _Mapping]] = ..., equip_data: _Optional[_Union[_stru_equip_data_pb2.EquipData, _Mapping]] = ..., fashion_data: _Optional[_Union[_stru_fashion_data_pb2.FashionData, _Mapping]] = ..., setting_data: _Optional[_Union[_stru_setting_data_pb2.SettingData, _Mapping]] = ..., scene_data: _Optional[_Union[_stru_scene_data_pb2.SceneData, _Mapping]] = ..., user_attr_data: _Optional[_Union[_stru_user_attr_data_pb2.UserAttrData, _Mapping]] = ..., team_data: _Optional[_Union[_stru_char_team_pb2.CharTeam, _Mapping]] = ..., union_data: _Optional[_Union[_stru_union_data_pb2.UnionData, _Mapping]] = ..., account_data: _Optional[_Union[_stru_account_data_pb2.AccountData, _Mapping]] = ..., function_data: _Optional[_Union[_stru_function_data_pb2.FunctionData, _Mapping]] = ..., personal_zone: _Optional[_Union[_stru_personal_zone_pb2.PersonalZone, _Mapping]] = ..., warehouse: _Optional[_Union[_stru_warehouse_data_pb2.WarehouseData, _Mapping]] = ..., season_rank: _Optional[_Union[_stru_season_rank_data_pb2.SeasonRankData, _Mapping]] = ..., fish_data: _Optional[_Union[_stru_fish_social_data_pb2.FishSocialData, _Mapping]] = ..., community_data: _Optional[_Union[_stru_community_data_pb2.CommunityData, _Mapping]] = ..., privilege_data: _Optional[_Union[_stru_privilege_data_pb2.PrivilegeData, _Mapping]] = ..., master_mode_dungeon_data: _Optional[_Union[_stru_master_mode_dungeon_data_pb2.MasterModeDungeonData, _Mapping]] = ...) -> None: ...
