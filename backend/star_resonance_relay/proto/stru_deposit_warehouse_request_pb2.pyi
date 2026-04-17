from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DepositWarehouseRequest(_message.Message):
    __slots__ = ("item_uuid", "item_num")
    ITEM_UUID_FIELD_NUMBER: _ClassVar[int]
    ITEM_NUM_FIELD_NUMBER: _ClassVar[int]
    item_uuid: int
    item_num: int
    def __init__(self, item_uuid: _Optional[int] = ..., item_num: _Optional[int] = ...) -> None: ...
