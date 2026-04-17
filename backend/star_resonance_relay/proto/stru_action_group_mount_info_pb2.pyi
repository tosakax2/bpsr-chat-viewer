from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ActionGroupMountInfo(_message.Message):
    __slots__ = ("mount_id", "mount_size")
    MOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    MOUNT_SIZE_FIELD_NUMBER: _ClassVar[int]
    mount_id: int
    mount_size: int
    def __init__(self, mount_id: _Optional[int] = ..., mount_size: _Optional[int] = ...) -> None: ...
