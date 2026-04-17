import stru_position_pb2 as _stru_position_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TeamMemberFastSyncData(_message.Message):
    __slots__ = ("char_id", "scene_id", "position", "hp", "max_hp", "state", "scene_area_id")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    HP_FIELD_NUMBER: _ClassVar[int]
    MAX_HP_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SCENE_AREA_ID_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    scene_id: int
    position: _stru_position_pb2.Position
    hp: int
    max_hp: int
    state: int
    scene_area_id: int
    def __init__(self, char_id: _Optional[int] = ..., scene_id: _Optional[int] = ..., position: _Optional[_Union[_stru_position_pb2.Position, _Mapping]] = ..., hp: _Optional[int] = ..., max_hp: _Optional[int] = ..., state: _Optional[int] = ..., scene_area_id: _Optional[int] = ...) -> None: ...
