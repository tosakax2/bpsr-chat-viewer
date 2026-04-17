import enum_e_match_ready_status_pb2 as _enum_e_match_ready_status_pb2
import enum_e_talent_job_type_pb2 as _enum_e_talent_job_type_pb2
import stru_match_player_show_info_pb2 as _stru_match_player_show_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MatchPlayerInfo(_message.Message):
    __slots__ = ("char_id", "ready_status", "profession_id", "talent_id", "is_assist", "is_bot", "match_show_info")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    READY_STATUS_FIELD_NUMBER: _ClassVar[int]
    PROFESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TALENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ASSIST_FIELD_NUMBER: _ClassVar[int]
    IS_BOT_FIELD_NUMBER: _ClassVar[int]
    MATCH_SHOW_INFO_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    ready_status: _enum_e_match_ready_status_pb2.EMatchReadyStatus
    profession_id: int
    talent_id: _enum_e_talent_job_type_pb2.ETalentJobType
    is_assist: bool
    is_bot: bool
    match_show_info: _stru_match_player_show_info_pb2.MatchPlayerShowInfo
    def __init__(self, char_id: _Optional[int] = ..., ready_status: _Optional[_Union[_enum_e_match_ready_status_pb2.EMatchReadyStatus, str]] = ..., profession_id: _Optional[int] = ..., talent_id: _Optional[_Union[_enum_e_talent_job_type_pb2.ETalentJobType, str]] = ..., is_assist: bool = ..., is_bot: bool = ..., match_show_info: _Optional[_Union[_stru_match_player_show_info_pb2.MatchPlayerShowInfo, _Mapping]] = ...) -> None: ...
