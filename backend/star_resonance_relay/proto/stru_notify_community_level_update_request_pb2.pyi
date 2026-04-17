from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyCommunityLevelUpdateRequest(_message.Message):
    __slots__ = ("new_level", "new_exp", "old_level", "old_exp", "old_resource", "new_resource")
    NEW_LEVEL_FIELD_NUMBER: _ClassVar[int]
    NEW_EXP_FIELD_NUMBER: _ClassVar[int]
    OLD_LEVEL_FIELD_NUMBER: _ClassVar[int]
    OLD_EXP_FIELD_NUMBER: _ClassVar[int]
    OLD_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    NEW_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    new_level: int
    new_exp: int
    old_level: int
    old_exp: int
    old_resource: int
    new_resource: int
    def __init__(self, new_level: _Optional[int] = ..., new_exp: _Optional[int] = ..., old_level: _Optional[int] = ..., old_exp: _Optional[int] = ..., old_resource: _Optional[int] = ..., new_resource: _Optional[int] = ...) -> None: ...
