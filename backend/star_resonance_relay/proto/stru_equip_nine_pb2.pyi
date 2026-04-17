from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EquipNine(_message.Message):
    __slots__ = ("slot", "equip_id")
    SLOT_FIELD_NUMBER: _ClassVar[int]
    EQUIP_ID_FIELD_NUMBER: _ClassVar[int]
    slot: int
    equip_id: int
    def __init__(self, slot: _Optional[int] = ..., equip_id: _Optional[int] = ...) -> None: ...
