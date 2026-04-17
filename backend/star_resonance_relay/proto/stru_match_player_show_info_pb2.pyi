import stru_avatar_info_pb2 as _stru_avatar_info_pb2
import enum_e_body_size_pb2 as _enum_e_body_size_pb2
import stru_personal_zone_show_pb2 as _stru_personal_zone_show_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MatchPlayerShowInfo(_message.Message):
    __slots__ = ("name", "gender", "body_size", "level", "avatar_info", "personal_zone")
    NAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    BODY_SIZE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    AVATAR_INFO_FIELD_NUMBER: _ClassVar[int]
    PERSONAL_ZONE_FIELD_NUMBER: _ClassVar[int]
    name: str
    gender: int
    body_size: _enum_e_body_size_pb2.EBodySize
    level: int
    avatar_info: _stru_avatar_info_pb2.AvatarInfo
    personal_zone: _stru_personal_zone_show_pb2.PersonalZoneShow
    def __init__(self, name: _Optional[str] = ..., gender: _Optional[int] = ..., body_size: _Optional[_Union[_enum_e_body_size_pb2.EBodySize, str]] = ..., level: _Optional[int] = ..., avatar_info: _Optional[_Union[_stru_avatar_info_pb2.AvatarInfo, _Mapping]] = ..., personal_zone: _Optional[_Union[_stru_personal_zone_show_pb2.PersonalZoneShow, _Mapping]] = ...) -> None: ...
