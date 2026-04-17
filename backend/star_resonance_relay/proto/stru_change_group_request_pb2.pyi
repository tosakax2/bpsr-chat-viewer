from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeGroupRequest(_message.Message):
    __slots__ = ("char_id", "target_group_id")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    target_group_id: int
    def __init__(self, char_id: _Optional[int] = ..., target_group_id: _Optional[int] = ...) -> None: ...
