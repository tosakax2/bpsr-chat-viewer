from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TransferInfo(_message.Message):
    __slots__ = ("target_scene_id", "target_pos_id")
    TARGET_SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_POS_ID_FIELD_NUMBER: _ClassVar[int]
    target_scene_id: int
    target_pos_id: int
    def __init__(self, target_scene_id: _Optional[int] = ..., target_pos_id: _Optional[int] = ...) -> None: ...
