import stru_dance_ball_pb2 as _stru_dance_ball_pb2
import stru_union_building_pb2 as _stru_union_building_pb2
import stru_union_e_screen_info_pb2 as _stru_union_e_screen_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonUnionInfo(_message.Message):
    __slots__ = ("union_id", "union_buildings", "e_screen_infos", "dance_ball")
    class UnionBuildingsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_union_building_pb2.UnionBuilding
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_union_building_pb2.UnionBuilding, _Mapping]] = ...) -> None: ...
    class EScreenInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_union_e_screen_info_pb2.UnionEScreenInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_union_e_screen_info_pb2.UnionEScreenInfo, _Mapping]] = ...) -> None: ...
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    UNION_BUILDINGS_FIELD_NUMBER: _ClassVar[int]
    E_SCREEN_INFOS_FIELD_NUMBER: _ClassVar[int]
    DANCE_BALL_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    union_buildings: _containers.MessageMap[int, _stru_union_building_pb2.UnionBuilding]
    e_screen_infos: _containers.MessageMap[int, _stru_union_e_screen_info_pb2.UnionEScreenInfo]
    dance_ball: _stru_dance_ball_pb2.DanceBall
    def __init__(self, union_id: _Optional[int] = ..., union_buildings: _Optional[_Mapping[int, _stru_union_building_pb2.UnionBuilding]] = ..., e_screen_infos: _Optional[_Mapping[int, _stru_union_e_screen_info_pb2.UnionEScreenInfo]] = ..., dance_ball: _Optional[_Union[_stru_dance_ball_pb2.DanceBall, _Mapping]] = ...) -> None: ...
