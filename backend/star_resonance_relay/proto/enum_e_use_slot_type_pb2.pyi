from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EUseSlotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UseSlotType_Other: _ClassVar[EUseSlotType]
    UseSlotType_Skill: _ClassVar[EUseSlotType]
UseSlotType_Other: EUseSlotType
UseSlotType_Skill: EUseSlotType
