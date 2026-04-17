import stru_position_pb2 as _stru_position_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LastSceneData(_message.Message):
    __slots__ = ("scene_id", "pos", "scene_area_id")
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    SCENE_AREA_ID_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    pos: _stru_position_pb2.Position
    scene_area_id: int
    def __init__(self, scene_id: _Optional[int] = ..., pos: _Optional[_Union[_stru_position_pb2.Position, _Mapping]] = ..., scene_area_id: _Optional[int] = ...) -> None: ...
