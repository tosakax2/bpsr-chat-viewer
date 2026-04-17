from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeGroupNameRequest(_message.Message):
    __slots__ = ("group_id", "new_name")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    new_name: str
    def __init__(self, group_id: _Optional[int] = ..., new_name: _Optional[str] = ...) -> None: ...
