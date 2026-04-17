import stru_position_pb2 as _stru_position_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScenePointInfo(_message.Message):
    __slots__ = ("position", "camera_id", "scene_area_id")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_AREA_ID_FIELD_NUMBER: _ClassVar[int]
    position: _stru_position_pb2.Position
    camera_id: int
    scene_area_id: int
    def __init__(self, position: _Optional[_Union[_stru_position_pb2.Position, _Mapping]] = ..., camera_id: _Optional[int] = ..., scene_area_id: _Optional[int] = ...) -> None: ...
