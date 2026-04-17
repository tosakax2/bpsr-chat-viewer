from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BindGroupWithTencentRequest(_message.Message):
    __slots__ = ("union_id", "group_type", "group_id")
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    group_type: int
    group_id: str
    def __init__(self, union_id: _Optional[int] = ..., group_type: _Optional[int] = ..., group_id: _Optional[str] = ...) -> None: ...
