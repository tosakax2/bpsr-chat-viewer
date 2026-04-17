import stru_season_role_level_pb2 as _stru_season_role_level_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SeasonRoleLevelData(_message.Message):
    __slots__ = ("season_role_level_map",)
    class SeasonRoleLevelMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_season_role_level_pb2.SeasonRoleLevel
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_season_role_level_pb2.SeasonRoleLevel, _Mapping]] = ...) -> None: ...
    SEASON_ROLE_LEVEL_MAP_FIELD_NUMBER: _ClassVar[int]
    season_role_level_map: _containers.MessageMap[int, _stru_season_role_level_pb2.SeasonRoleLevel]
    def __init__(self, season_role_level_map: _Optional[_Mapping[int, _stru_season_role_level_pb2.SeasonRoleLevel]] = ...) -> None: ...
