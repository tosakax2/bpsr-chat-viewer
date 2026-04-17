from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ScenePosIdInfo(_message.Message):
    __slots__ = ("scene_pos_id",)
    SCENE_POS_ID_FIELD_NUMBER: _ClassVar[int]
    scene_pos_id: int
    def __init__(self, scene_pos_id: _Optional[int] = ...) -> None: ...
