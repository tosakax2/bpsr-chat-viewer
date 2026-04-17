import stru_avatar_info_pb2 as _stru_avatar_info_pb2
import enum_e_hero_key_roll_type_pb2 as _enum_e_hero_key_roll_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeroKeyRollInfo(_message.Message):
    __slots__ = ("type", "char_id", "name", "avatar", "roll_value")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    ROLL_VALUE_FIELD_NUMBER: _ClassVar[int]
    type: _enum_e_hero_key_roll_type_pb2.EHeroKeyRollType
    char_id: int
    name: str
    avatar: _stru_avatar_info_pb2.AvatarInfo
    roll_value: int
    def __init__(self, type: _Optional[_Union[_enum_e_hero_key_roll_type_pb2.EHeroKeyRollType, str]] = ..., char_id: _Optional[int] = ..., name: _Optional[str] = ..., avatar: _Optional[_Union[_stru_avatar_info_pb2.AvatarInfo, _Mapping]] = ..., roll_value: _Optional[int] = ...) -> None: ...
