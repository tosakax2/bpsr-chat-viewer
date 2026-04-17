import stru_cut_scene_point_info_pb2 as _stru_cut_scene_point_info_pb2
import stru_scene_point_info_pb2 as _stru_scene_point_info_pb2
import stru_scene_pos_id_info_pb2 as _stru_scene_pos_id_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PositionParam(_message.Message):
    __slots__ = ("scene_point_info", "scene_pos_info", "cut_scene_point_info")
    SCENE_POINT_INFO_FIELD_NUMBER: _ClassVar[int]
    SCENE_POS_INFO_FIELD_NUMBER: _ClassVar[int]
    CUT_SCENE_POINT_INFO_FIELD_NUMBER: _ClassVar[int]
    scene_point_info: _stru_scene_point_info_pb2.ScenePointInfo
    scene_pos_info: _stru_scene_pos_id_info_pb2.ScenePosIdInfo
    cut_scene_point_info: _stru_cut_scene_point_info_pb2.CutScenePointInfo
    def __init__(self, scene_point_info: _Optional[_Union[_stru_scene_point_info_pb2.ScenePointInfo, _Mapping]] = ..., scene_pos_info: _Optional[_Union[_stru_scene_pos_id_info_pb2.ScenePosIdInfo, _Mapping]] = ..., cut_scene_point_info: _Optional[_Union[_stru_cut_scene_point_info_pb2.CutScenePointInfo, _Mapping]] = ...) -> None: ...
