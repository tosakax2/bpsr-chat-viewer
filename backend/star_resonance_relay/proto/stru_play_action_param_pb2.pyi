from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayActionParam(_message.Message):
    __slots__ = ("action_id", "is_upper", "is_dance_together", "mount_id", "mount_size")
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_UPPER_FIELD_NUMBER: _ClassVar[int]
    IS_DANCE_TOGETHER_FIELD_NUMBER: _ClassVar[int]
    MOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    MOUNT_SIZE_FIELD_NUMBER: _ClassVar[int]
    action_id: int
    is_upper: bool
    is_dance_together: bool
    mount_id: int
    mount_size: int
    def __init__(self, action_id: _Optional[int] = ..., is_upper: bool = ..., is_dance_together: bool = ..., mount_id: _Optional[int] = ..., mount_size: _Optional[int] = ...) -> None: ...
