from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetMailListRequest(_message.Message):
    __slots__ = ("page", "importance", "is_collect")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    IMPORTANCE_FIELD_NUMBER: _ClassVar[int]
    IS_COLLECT_FIELD_NUMBER: _ClassVar[int]
    page: int
    importance: int
    is_collect: bool
    def __init__(self, page: _Optional[int] = ..., importance: _Optional[int] = ..., is_collect: bool = ...) -> None: ...
