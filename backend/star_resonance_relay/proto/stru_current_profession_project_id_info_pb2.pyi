from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CurrentProfessionProjectIdInfo(_message.Message):
    __slots__ = ("current_profession_project_id",)
    CURRENT_PROFESSION_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    current_profession_project_id: int
    def __init__(self, current_profession_project_id: _Optional[int] = ...) -> None: ...
