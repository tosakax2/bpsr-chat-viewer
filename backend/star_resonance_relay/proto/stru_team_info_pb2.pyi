import stru_team_base_info_pb2 as _stru_team_base_info_pb2
import stru_team_mem_data_pb2 as _stru_team_mem_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TeamInfo(_message.Message):
    __slots__ = ("team_id", "members", "base_info")
    class MembersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_team_mem_data_pb2.TeamMemData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_team_mem_data_pb2.TeamMemData, _Mapping]] = ...) -> None: ...
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    BASE_INFO_FIELD_NUMBER: _ClassVar[int]
    team_id: int
    members: _containers.MessageMap[int, _stru_team_mem_data_pb2.TeamMemData]
    base_info: _stru_team_base_info_pb2.TeamBaseInfo
    def __init__(self, team_id: _Optional[int] = ..., members: _Optional[_Mapping[int, _stru_team_mem_data_pb2.TeamMemData]] = ..., base_info: _Optional[_Union[_stru_team_base_info_pb2.TeamBaseInfo, _Mapping]] = ...) -> None: ...
