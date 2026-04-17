import stru_scene_personal_object_pb2 as _stru_scene_personal_object_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PersonalObject(_message.Message):
    __slots__ = ("scene_obj_data",)
    class SceneObjDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_scene_personal_object_pb2.ScenePersonalObject
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_scene_personal_object_pb2.ScenePersonalObject, _Mapping]] = ...) -> None: ...
    SCENE_OBJ_DATA_FIELD_NUMBER: _ClassVar[int]
    scene_obj_data: _containers.MessageMap[int, _stru_scene_personal_object_pb2.ScenePersonalObject]
    def __init__(self, scene_obj_data: _Optional[_Mapping[int, _stru_scene_personal_object_pb2.ScenePersonalObject]] = ...) -> None: ...
