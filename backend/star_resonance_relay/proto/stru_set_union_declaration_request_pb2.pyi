from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetUnionDeclarationRequest(_message.Message):
    __slots__ = ("union_id", "declaration")
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    DECLARATION_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    declaration: str
    def __init__(self, union_id: _Optional[int] = ..., declaration: _Optional[str] = ...) -> None: ...
