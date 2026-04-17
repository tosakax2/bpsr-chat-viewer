from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EquipInfo(_message.Message):
    __slots__ = ("equip_slot", "item_uuid", "equip_slot_refine_level", "equip_slot_refine_failed_count")
    EQUIP_SLOT_FIELD_NUMBER: _ClassVar[int]
    ITEM_UUID_FIELD_NUMBER: _ClassVar[int]
    EQUIP_SLOT_REFINE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    EQUIP_SLOT_REFINE_FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    equip_slot: int
    item_uuid: int
    equip_slot_refine_level: int
    equip_slot_refine_failed_count: int
    def __init__(self, equip_slot: _Optional[int] = ..., item_uuid: _Optional[int] = ..., equip_slot_refine_level: _Optional[int] = ..., equip_slot_refine_failed_count: _Optional[int] = ...) -> None: ...
