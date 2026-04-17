import stru_team_base_info_pb2 as _stru_team_base_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NoticeUpdateTeamInfoRequest(_message.Message):
    __slots__ = ("base_info",)
    BASE_INFO_FIELD_NUMBER: _ClassVar[int]
    base_info: _stru_team_base_info_pb2.TeamBaseInfo
    def __init__(self, base_info: _Optional[_Union[_stru_team_base_info_pb2.TeamBaseInfo, _Mapping]] = ...) -> None: ...
