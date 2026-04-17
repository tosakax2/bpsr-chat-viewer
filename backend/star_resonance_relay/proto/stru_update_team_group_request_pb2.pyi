from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateTeamGroupRequest(_message.Message):
    __slots__ = ("group_id", "char_id", "group_index")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_INDEX_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    char_id: int
    group_index: int
    def __init__(self, group_id: _Optional[int] = ..., char_id: _Optional[int] = ..., group_index: _Optional[int] = ...) -> None: ...
