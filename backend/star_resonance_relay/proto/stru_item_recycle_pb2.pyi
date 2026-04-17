from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ItemRecycle(_message.Message):
    __slots__ = ("recycle_id", "item_uuid", "count")
    RECYCLE_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_UUID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    recycle_id: int
    item_uuid: int
    count: int
    def __init__(self, recycle_id: _Optional[int] = ..., item_uuid: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
