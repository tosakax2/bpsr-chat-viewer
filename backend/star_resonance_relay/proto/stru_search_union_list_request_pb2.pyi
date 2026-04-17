from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SearchUnionListRequest(_message.Message):
    __slots__ = ("search_content",)
    SEARCH_CONTENT_FIELD_NUMBER: _ClassVar[int]
    search_content: str
    def __init__(self, search_content: _Optional[str] = ...) -> None: ...
