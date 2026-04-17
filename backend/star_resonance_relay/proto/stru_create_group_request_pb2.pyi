from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateGroupRequest(_message.Message):
    __slots__ = ("group_name",)
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    group_name: str
    def __init__(self, group_name: _Optional[str] = ...) -> None: ...
