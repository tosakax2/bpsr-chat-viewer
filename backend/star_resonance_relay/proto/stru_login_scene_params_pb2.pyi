from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LoginSceneParams(_message.Message):
    __slots__ = ("into_scene_type", "last_scene_id", "born_scene_id")
    INTO_SCENE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LAST_SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    BORN_SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    into_scene_type: int
    last_scene_id: int
    born_scene_id: int
    def __init__(self, into_scene_type: _Optional[int] = ..., last_scene_id: _Optional[int] = ..., born_scene_id: _Optional[int] = ...) -> None: ...
