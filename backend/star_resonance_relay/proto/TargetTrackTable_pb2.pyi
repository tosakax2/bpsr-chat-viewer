from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TargetTrackTableBase(_message.Message):
    __slots__ = ("id", "type", "team", "scene_track", "map_track", "start_distance", "end_distance", "icon")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    SCENE_TRACK_FIELD_NUMBER: _ClassVar[int]
    MAP_TRACK_FIELD_NUMBER: _ClassVar[int]
    START_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    END_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: str
    team: int
    scene_track: int
    map_track: int
    start_distance: int
    end_distance: int
    icon: str
    def __init__(self, id: _Optional[int] = ..., type: _Optional[str] = ..., team: _Optional[int] = ..., scene_track: _Optional[int] = ..., map_track: _Optional[int] = ..., start_distance: _Optional[int] = ..., end_distance: _Optional[int] = ..., icon: _Optional[str] = ...) -> None: ...

class TargetTrackTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TargetTrackTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TargetTrackTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, TargetTrackTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, TargetTrackTableBase]] = ...) -> None: ...
