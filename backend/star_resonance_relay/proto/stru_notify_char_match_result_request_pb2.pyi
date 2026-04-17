import stru_team_info_pb2 as _stru_team_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyCharMatchResultRequest(_message.Message):
    __slots__ = ("success", "team_info")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    TEAM_INFO_FIELD_NUMBER: _ClassVar[int]
    success: bool
    team_info: _stru_team_info_pb2.TeamInfo
    def __init__(self, success: bool = ..., team_info: _Optional[_Union[_stru_team_info_pb2.TeamInfo, _Mapping]] = ...) -> None: ...
