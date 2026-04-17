import stru_item_pb2 as _stru_item_pb2
import stru_scene_info_pb2 as _stru_scene_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TeamActivityDungeonInfo(_message.Message):
    __slots__ = ("scene_info", "use_item")
    SCENE_INFO_FIELD_NUMBER: _ClassVar[int]
    USE_ITEM_FIELD_NUMBER: _ClassVar[int]
    scene_info: _stru_scene_info_pb2.SceneInfo
    use_item: _stru_item_pb2.Item
    def __init__(self, scene_info: _Optional[_Union[_stru_scene_info_pb2.SceneInfo, _Mapping]] = ..., use_item: _Optional[_Union[_stru_item_pb2.Item, _Mapping]] = ...) -> None: ...
