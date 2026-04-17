from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ESlotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NormalSlot: _ClassVar[ESlotType]
    PressTimeSlot: _ClassVar[ESlotType]
    StageHasLongPressSlot: _ClassVar[ESlotType]
NormalSlot: ESlotType
PressTimeSlot: ESlotType
StageHasLongPressSlot: ESlotType
