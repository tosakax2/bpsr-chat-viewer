from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SortItemParam(_message.Message):
    __slots__ = ("src_item_uuid", "dst_item_uuid")
    SRC_ITEM_UUID_FIELD_NUMBER: _ClassVar[int]
    DST_ITEM_UUID_FIELD_NUMBER: _ClassVar[int]
    src_item_uuid: int
    dst_item_uuid: int
    def __init__(self, src_item_uuid: _Optional[int] = ..., dst_item_uuid: _Optional[int] = ...) -> None: ...
