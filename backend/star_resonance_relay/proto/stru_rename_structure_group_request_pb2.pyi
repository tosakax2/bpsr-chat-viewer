from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RenameStructureGroupRequest(_message.Message):
    __slots__ = ("group_id", "group_name", "is_outer")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_OUTER_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    group_name: str
    is_outer: bool
    def __init__(self, group_id: _Optional[int] = ..., group_name: _Optional[str] = ..., is_outer: bool = ...) -> None: ...
