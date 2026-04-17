from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SwitchProjectRequest(_message.Message):
    __slots__ = ("old_project_id", "new_project_id")
    OLD_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    old_project_id: int
    new_project_id: int
    def __init__(self, old_project_id: _Optional[int] = ..., new_project_id: _Optional[int] = ...) -> None: ...
