from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GashaWishSelectionRequest(_message.Message):
    __slots__ = ("pool_id", "wish_id")
    POOL_ID_FIELD_NUMBER: _ClassVar[int]
    WISH_ID_FIELD_NUMBER: _ClassVar[int]
    pool_id: int
    wish_id: int
    def __init__(self, pool_id: _Optional[int] = ..., wish_id: _Optional[int] = ...) -> None: ...
