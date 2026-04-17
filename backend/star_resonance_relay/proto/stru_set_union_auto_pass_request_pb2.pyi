from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetUnionAutoPassRequest(_message.Message):
    __slots__ = ("union_id", "auto_pass")
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    AUTO_PASS_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    auto_pass: bool
    def __init__(self, union_id: _Optional[int] = ..., auto_pass: bool = ...) -> None: ...
