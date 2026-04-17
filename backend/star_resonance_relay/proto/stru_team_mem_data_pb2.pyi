import stru_team_member_social_data_pb2 as _stru_team_member_social_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TeamMemData(_message.Message):
    __slots__ = ("char_id", "enter_time", "call_status", "talent_id", "online_status", "scene_id", "voice_is_open", "group_id", "social_data")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    ENTER_TIME_FIELD_NUMBER: _ClassVar[int]
    CALL_STATUS_FIELD_NUMBER: _ClassVar[int]
    TALENT_ID_FIELD_NUMBER: _ClassVar[int]
    ONLINE_STATUS_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    VOICE_IS_OPEN_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_DATA_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    enter_time: int
    call_status: int
    talent_id: int
    online_status: int
    scene_id: int
    voice_is_open: bool
    group_id: int
    social_data: _stru_team_member_social_data_pb2.TeamMemberSocialData
    def __init__(self, char_id: _Optional[int] = ..., enter_time: _Optional[int] = ..., call_status: _Optional[int] = ..., talent_id: _Optional[int] = ..., online_status: _Optional[int] = ..., scene_id: _Optional[int] = ..., voice_is_open: bool = ..., group_id: _Optional[int] = ..., social_data: _Optional[_Union[_stru_team_member_social_data_pb2.TeamMemberSocialData, _Mapping]] = ...) -> None: ...
