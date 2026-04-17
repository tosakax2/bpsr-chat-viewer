import stru_cut_scene_info_pb2 as _stru_cut_scene_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CutSceneInfos(_message.Message):
    __slots__ = ("cut_scene_infos", "finished_cut_scenes", "finished_infos")
    class CutSceneInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_cut_scene_info_pb2.CutSceneInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_cut_scene_info_pb2.CutSceneInfo, _Mapping]] = ...) -> None: ...
    class FinishedCutScenesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class FinishedInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    CUT_SCENE_INFOS_FIELD_NUMBER: _ClassVar[int]
    FINISHED_CUT_SCENES_FIELD_NUMBER: _ClassVar[int]
    FINISHED_INFOS_FIELD_NUMBER: _ClassVar[int]
    cut_scene_infos: _containers.MessageMap[int, _stru_cut_scene_info_pb2.CutSceneInfo]
    finished_cut_scenes: _containers.ScalarMap[int, bool]
    finished_infos: _containers.ScalarMap[int, bool]
    def __init__(self, cut_scene_infos: _Optional[_Mapping[int, _stru_cut_scene_info_pb2.CutSceneInfo]] = ..., finished_cut_scenes: _Optional[_Mapping[int, bool]] = ..., finished_infos: _Optional[_Mapping[int, bool]] = ...) -> None: ...
