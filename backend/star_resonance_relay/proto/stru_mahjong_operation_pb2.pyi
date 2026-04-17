from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MahjongOperation(_message.Message):
    __slots__ = ("handle", "index", "card", "card_index", "count_index")
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    CARD_FIELD_NUMBER: _ClassVar[int]
    CARD_INDEX_FIELD_NUMBER: _ClassVar[int]
    COUNT_INDEX_FIELD_NUMBER: _ClassVar[int]
    handle: int
    index: int
    card: int
    card_index: int
    count_index: int
    def __init__(self, handle: _Optional[int] = ..., index: _Optional[int] = ..., card: _Optional[int] = ..., card_index: _Optional[int] = ..., count_index: _Optional[int] = ...) -> None: ...
