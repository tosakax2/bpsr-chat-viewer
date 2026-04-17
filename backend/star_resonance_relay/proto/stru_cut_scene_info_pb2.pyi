import stru_event_data_pb2 as _stru_event_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CutSceneInfo(_message.Message):
    __slots__ = ("cut_scene_id", "flag", "scene_id", "event_data")
    CUT_SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    cut_scene_id: int
    flag: int
    scene_id: int
    event_data: _stru_event_data_pb2.EventData
    def __init__(self, cut_scene_id: _Optional[int] = ..., flag: _Optional[int] = ..., scene_id: _Optional[int] = ..., event_data: _Optional[_Union[_stru_event_data_pb2.EventData, _Mapping]] = ...) -> None: ...
