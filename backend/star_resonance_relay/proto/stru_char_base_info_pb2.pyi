import stru_avatar_info_pb2 as _stru_avatar_info_pb2
import stru_char_team_pb2 as _stru_char_team_pb2
import enum_e_body_size_pb2 as _enum_e_body_size_pb2
import enum_e_gender_pb2 as _enum_e_gender_pb2
import stru_face_data_pb2 as _stru_face_data_pb2
import stru_profile_info_pb2 as _stru_profile_info_pb2
import stru_user_union_pb2 as _stru_user_union_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CharBaseInfo(_message.Message):
    __slots__ = ("char_id", "account_id", "show_id", "server_id", "name", "gender", "is_deleted", "is_forbid", "is_mute", "x", "y", "z", "dir", "face_data", "card_id", "create_time", "online_time", "offline_time", "profile_info", "team_info", "char_state", "body_size", "union_info", "personal_state", "avatar_info", "total_online_time", "open_id", "sdk_type", "os", "init_profession_id", "last_cal_total_time", "area_id", "client_version", "fight_point", "sum_save", "client_resource_version", "last_offline_time", "day_acc_dur_time", "last_acc_dur_timestamp", "last_online_time")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SHOW_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    IS_FORBID_FIELD_NUMBER: _ClassVar[int]
    IS_MUTE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    DIR_FIELD_NUMBER: _ClassVar[int]
    FACE_DATA_FIELD_NUMBER: _ClassVar[int]
    CARD_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ONLINE_TIME_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_TIME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_INFO_FIELD_NUMBER: _ClassVar[int]
    TEAM_INFO_FIELD_NUMBER: _ClassVar[int]
    CHAR_STATE_FIELD_NUMBER: _ClassVar[int]
    BODY_SIZE_FIELD_NUMBER: _ClassVar[int]
    UNION_INFO_FIELD_NUMBER: _ClassVar[int]
    PERSONAL_STATE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_INFO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ONLINE_TIME_FIELD_NUMBER: _ClassVar[int]
    OPEN_ID_FIELD_NUMBER: _ClassVar[int]
    SDK_TYPE_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    INIT_PROFESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_CAL_TOTAL_TIME_FIELD_NUMBER: _ClassVar[int]
    AREA_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    FIGHT_POINT_FIELD_NUMBER: _ClassVar[int]
    SUM_SAVE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    LAST_OFFLINE_TIME_FIELD_NUMBER: _ClassVar[int]
    DAY_ACC_DUR_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_ACC_DUR_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LAST_ONLINE_TIME_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    account_id: str
    show_id: int
    server_id: int
    name: str
    gender: _enum_e_gender_pb2.EGender
    is_deleted: bool
    is_forbid: bool
    is_mute: bool
    x: float
    y: float
    z: float
    dir: float
    face_data: _stru_face_data_pb2.FaceData
    card_id: int
    create_time: int
    online_time: int
    offline_time: int
    profile_info: _stru_profile_info_pb2.ProfileInfo
    team_info: _stru_char_team_pb2.CharTeam
    char_state: int
    body_size: _enum_e_body_size_pb2.EBodySize
    union_info: _stru_user_union_pb2.UserUnion
    personal_state: _containers.RepeatedScalarFieldContainer[int]
    avatar_info: _stru_avatar_info_pb2.AvatarInfo
    total_online_time: int
    open_id: str
    sdk_type: int
    os: int
    init_profession_id: int
    last_cal_total_time: int
    area_id: int
    client_version: str
    fight_point: int
    sum_save: int
    client_resource_version: str
    last_offline_time: int
    day_acc_dur_time: int
    last_acc_dur_timestamp: int
    last_online_time: int
    def __init__(self, char_id: _Optional[int] = ..., account_id: _Optional[str] = ..., show_id: _Optional[int] = ..., server_id: _Optional[int] = ..., name: _Optional[str] = ..., gender: _Optional[_Union[_enum_e_gender_pb2.EGender, str]] = ..., is_deleted: bool = ..., is_forbid: bool = ..., is_mute: bool = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., dir: _Optional[float] = ..., face_data: _Optional[_Union[_stru_face_data_pb2.FaceData, _Mapping]] = ..., card_id: _Optional[int] = ..., create_time: _Optional[int] = ..., online_time: _Optional[int] = ..., offline_time: _Optional[int] = ..., profile_info: _Optional[_Union[_stru_profile_info_pb2.ProfileInfo, _Mapping]] = ..., team_info: _Optional[_Union[_stru_char_team_pb2.CharTeam, _Mapping]] = ..., char_state: _Optional[int] = ..., body_size: _Optional[_Union[_enum_e_body_size_pb2.EBodySize, str]] = ..., union_info: _Optional[_Union[_stru_user_union_pb2.UserUnion, _Mapping]] = ..., personal_state: _Optional[_Iterable[int]] = ..., avatar_info: _Optional[_Union[_stru_avatar_info_pb2.AvatarInfo, _Mapping]] = ..., total_online_time: _Optional[int] = ..., open_id: _Optional[str] = ..., sdk_type: _Optional[int] = ..., os: _Optional[int] = ..., init_profession_id: _Optional[int] = ..., last_cal_total_time: _Optional[int] = ..., area_id: _Optional[int] = ..., client_version: _Optional[str] = ..., fight_point: _Optional[int] = ..., sum_save: _Optional[int] = ..., client_resource_version: _Optional[str] = ..., last_offline_time: _Optional[int] = ..., day_acc_dur_time: _Optional[int] = ..., last_acc_dur_timestamp: _Optional[int] = ..., last_online_time: _Optional[int] = ...) -> None: ...
