from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EquipBreachRequest(_message.Message):
    __slots__ = ("equip_uid",)
    EQUIP_UID_FIELD_NUMBER: _ClassVar[int]
    equip_uid: int
    def __init__(self, equip_uid: _Optional[int] = ...) -> None: ...
