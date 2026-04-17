from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonReadyItemInfo(_message.Message):
    __slots__ = ("item_id", "item_num")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_NUM_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    item_num: int
    def __init__(self, item_id: _Optional[int] = ..., item_num: _Optional[int] = ...) -> None: ...
