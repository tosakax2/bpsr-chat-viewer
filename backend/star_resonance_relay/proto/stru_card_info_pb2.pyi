import stru_char_team_pb2 as _stru_char_team_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CardInfo(_message.Message):
    __slots__ = ("char_id", "name", "model_id", "team_info", "is_friend", "union_name", "union_id", "role_level", "gender", "offline_time")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_FRIEND_FIELD_NUMBER: _ClassVar[int]
    UNION_NAME_FIELD_NUMBER: _ClassVar[int]
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_TIME_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    name: str
    model_id: int
    team_info: _stru_char_team_pb2.CharTeam
    is_friend: bool
    union_name: str
    union_id: int
    role_level: int
    gender: int
    offline_time: int
    def __init__(self, char_id: _Optional[int] = ..., name: _Optional[str] = ..., model_id: _Optional[int] = ..., team_info: _Optional[_Union[_stru_char_team_pb2.CharTeam, _Mapping]] = ..., is_friend: bool = ..., union_name: _Optional[str] = ..., union_id: _Optional[int] = ..., role_level: _Optional[int] = ..., gender: _Optional[int] = ..., offline_time: _Optional[int] = ...) -> None: ...
