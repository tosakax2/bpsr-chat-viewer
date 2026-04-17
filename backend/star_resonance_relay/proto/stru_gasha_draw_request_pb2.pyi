from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GashaDrawRequest(_message.Message):
    __slots__ = ("count", "pool_id")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    count: int
    pool_id: int
    def __init__(self, count: _Optional[int] = ..., pool_id: _Optional[int] = ...) -> None: ...
