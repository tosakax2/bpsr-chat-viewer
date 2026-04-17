import enum_e_body_size_pb2 as _enum_e_body_size_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BasicData(_message.Message):
    __slots__ = ("char_id", "show_id", "name", "gender", "body_size", "level", "scene_id", "personal_state", "offline_time", "scene_guid", "create_time", "cur_talent_pool_id", "bot_ai_id", "register_channel", "char_state", "online_time", "sum_save_diamond", "is_newbie", "season_level", "is_backflow")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    SHOW_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    BODY_SIZE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    PERSONAL_STATE_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_TIME_FIELD_NUMBER: _ClassVar[int]
    SCENE_GUID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CUR_TALENT_POOL_ID_FIELD_NUMBER: _ClassVar[int]
    BOT_AI_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTER_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CHAR_STATE_FIELD_NUMBER: _ClassVar[int]
    ONLINE_TIME_FIELD_NUMBER: _ClassVar[int]
    SUM_SAVE_DIAMOND_FIELD_NUMBER: _ClassVar[int]
    IS_NEWBIE_FIELD_NUMBER: _ClassVar[int]
    SEASON_LEVEL_FIELD_NUMBER: _ClassVar[int]
    IS_BACKFLOW_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    show_id: int
    name: str
    gender: int
    body_size: _enum_e_body_size_pb2.EBodySize
    level: int
    scene_id: int
    personal_state: _containers.RepeatedScalarFieldContainer[int]
    offline_time: int
    scene_guid: str
    create_time: int
    cur_talent_pool_id: int
    bot_ai_id: int
    register_channel: int
    char_state: int
    online_time: int
    sum_save_diamond: int
    is_newbie: bool
    season_level: int
    is_backflow: bool
    def __init__(self, char_id: _Optional[int] = ..., show_id: _Optional[int] = ..., name: _Optional[str] = ..., gender: _Optional[int] = ..., body_size: _Optional[_Union[_enum_e_body_size_pb2.EBodySize, str]] = ..., level: _Optional[int] = ..., scene_id: _Optional[int] = ..., personal_state: _Optional[_Iterable[int]] = ..., offline_time: _Optional[int] = ..., scene_guid: _Optional[str] = ..., create_time: _Optional[int] = ..., cur_talent_pool_id: _Optional[int] = ..., bot_ai_id: _Optional[int] = ..., register_channel: _Optional[int] = ..., char_state: _Optional[int] = ..., online_time: _Optional[int] = ..., sum_save_diamond: _Optional[int] = ..., is_newbie: bool = ..., season_level: _Optional[int] = ..., is_backflow: bool = ...) -> None: ...
