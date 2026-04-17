from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlaceHolderScenePosition(_message.Message):
    __slots__ = ("scene_id", "line_id", "positionx", "positiony", "positionz", "map_layer_id")
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    LINE_ID_FIELD_NUMBER: _ClassVar[int]
    POSITIONX_FIELD_NUMBER: _ClassVar[int]
    POSITIONY_FIELD_NUMBER: _ClassVar[int]
    POSITIONZ_FIELD_NUMBER: _ClassVar[int]
    MAP_LAYER_ID_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    line_id: int
    positionx: int
    positiony: int
    positionz: int
    map_layer_id: int
    def __init__(self, scene_id: _Optional[int] = ..., line_id: _Optional[int] = ..., positionx: _Optional[int] = ..., positiony: _Optional[int] = ..., positionz: _Optional[int] = ..., map_layer_id: _Optional[int] = ...) -> None: ...
