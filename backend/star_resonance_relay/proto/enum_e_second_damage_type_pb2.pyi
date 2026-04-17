from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ESecondDamageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ESecondDamageType_Crit: _ClassVar[ESecondDamageType]
    ESecondDamageType_Block: _ClassVar[ESecondDamageType]
    ESecondDamageType_AttackerLuck: _ClassVar[ESecondDamageType]
    ESecondDamageType_AttackedLuck: _ClassVar[ESecondDamageType]
ESecondDamageType_Crit: ESecondDamageType
ESecondDamageType_Block: ESecondDamageType
ESecondDamageType_AttackerLuck: ESecondDamageType
ESecondDamageType_AttackedLuck: ESecondDamageType
