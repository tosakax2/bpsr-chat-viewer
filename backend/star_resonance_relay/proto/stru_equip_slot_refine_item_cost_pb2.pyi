from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EquipSlotRefineItemCost(_message.Message):
    __slots__ = ("item_config_id", "item_count")
    ITEM_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    item_config_id: int
    item_count: int
    def __init__(self, item_config_id: _Optional[int] = ..., item_count: _Optional[int] = ...) -> None: ...
