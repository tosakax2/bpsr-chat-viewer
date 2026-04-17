import stru_avatar_info_pb2 as _stru_avatar_info_pb2
import stru_basic_data_pb2 as _stru_basic_data_pb2
import stru_equip_data_pb2 as _stru_equip_data_pb2
import stru_face_data_pb2 as _stru_face_data_pb2
import stru_fashion_data_pb2 as _stru_fashion_data_pb2
import stru_personal_zone_show_pb2 as _stru_personal_zone_show_pb2
import stru_profession_data_pb2 as _stru_profession_data_pb2
import stru_user_attr_data_pb2 as _stru_user_attr_data_pb2
import stru_user_scene_info_pb2 as _stru_user_scene_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TeamMemberSocialData(_message.Message):
    __slots__ = ("basic_data", "avatar_info", "face_data", "profession_data", "equip_data", "fashion_data", "user_scene_info", "user_attr_data", "personal_zone")
    BASIC_DATA_FIELD_NUMBER: _ClassVar[int]
    AVATAR_INFO_FIELD_NUMBER: _ClassVar[int]
    FACE_DATA_FIELD_NUMBER: _ClassVar[int]
    PROFESSION_DATA_FIELD_NUMBER: _ClassVar[int]
    EQUIP_DATA_FIELD_NUMBER: _ClassVar[int]
    FASHION_DATA_FIELD_NUMBER: _ClassVar[int]
    USER_SCENE_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_ATTR_DATA_FIELD_NUMBER: _ClassVar[int]
    PERSONAL_ZONE_FIELD_NUMBER: _ClassVar[int]
    basic_data: _stru_basic_data_pb2.BasicData
    avatar_info: _stru_avatar_info_pb2.AvatarInfo
    face_data: _stru_face_data_pb2.FaceData
    profession_data: _stru_profession_data_pb2.ProfessionData
    equip_data: _stru_equip_data_pb2.EquipData
    fashion_data: _stru_fashion_data_pb2.FashionData
    user_scene_info: _stru_user_scene_info_pb2.UserSceneInfo
    user_attr_data: _stru_user_attr_data_pb2.UserAttrData
    personal_zone: _stru_personal_zone_show_pb2.PersonalZoneShow
    def __init__(self, basic_data: _Optional[_Union[_stru_basic_data_pb2.BasicData, _Mapping]] = ..., avatar_info: _Optional[_Union[_stru_avatar_info_pb2.AvatarInfo, _Mapping]] = ..., face_data: _Optional[_Union[_stru_face_data_pb2.FaceData, _Mapping]] = ..., profession_data: _Optional[_Union[_stru_profession_data_pb2.ProfessionData, _Mapping]] = ..., equip_data: _Optional[_Union[_stru_equip_data_pb2.EquipData, _Mapping]] = ..., fashion_data: _Optional[_Union[_stru_fashion_data_pb2.FashionData, _Mapping]] = ..., user_scene_info: _Optional[_Union[_stru_user_scene_info_pb2.UserSceneInfo, _Mapping]] = ..., user_attr_data: _Optional[_Union[_stru_user_attr_data_pb2.UserAttrData, _Mapping]] = ..., personal_zone: _Optional[_Union[_stru_personal_zone_show_pb2.PersonalZoneShow, _Mapping]] = ...) -> None: ...
