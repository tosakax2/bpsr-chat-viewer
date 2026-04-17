import enum_e_scene_line_status_pb2 as _enum_e_scene_line_status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SceneLineData(_message.Message):
    __slots__ = ("line_id", "status", "scene_guid")
    LINE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SCENE_GUID_FIELD_NUMBER: _ClassVar[int]
    line_id: int
    status: _enum_e_scene_line_status_pb2.ESceneLineStatus
    scene_guid: str
    def __init__(self, line_id: _Optional[int] = ..., status: _Optional[_Union[_enum_e_scene_line_status_pb2.ESceneLineStatus, str]] = ..., scene_guid: _Optional[str] = ...) -> None: ...
