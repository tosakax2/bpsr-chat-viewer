from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateUnionRequest(_message.Message):
    __slots__ = ("union_name", "union_icon", "declaration", "auto_approval", "tags")
    UNION_NAME_FIELD_NUMBER: _ClassVar[int]
    UNION_ICON_FIELD_NUMBER: _ClassVar[int]
    DECLARATION_FIELD_NUMBER: _ClassVar[int]
    AUTO_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    union_name: str
    union_icon: _containers.RepeatedScalarFieldContainer[int]
    declaration: str
    auto_approval: bool
    tags: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, union_name: _Optional[str] = ..., union_icon: _Optional[_Iterable[int]] = ..., declaration: _Optional[str] = ..., auto_approval: bool = ..., tags: _Optional[_Iterable[int]] = ...) -> None: ...
