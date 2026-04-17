from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UserSceneInfo(_message.Message):
    __slots__ = ("scene_id", "scene_guid", "line_id")
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    SCENE_GUID_FIELD_NUMBER: _ClassVar[int]
    LINE_ID_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    scene_guid: str
    line_id: int
    def __init__(self, scene_id: _Optional[int] = ..., scene_guid: _Optional[str] = ..., line_id: _Optional[int] = ...) -> None: ...
