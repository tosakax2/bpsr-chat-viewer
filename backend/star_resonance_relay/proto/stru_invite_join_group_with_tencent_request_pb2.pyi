from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InviteJoinGroupWithTencentRequest(_message.Message):
    __slots__ = ("union_id", "desc", "url")
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    desc: str
    url: str
    def __init__(self, union_id: _Optional[int] = ..., desc: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
