from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ETalentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TalentType_None: _ClassVar[ETalentType]
    TalentType_Active: _ClassVar[ETalentType]
    TalentType_SmallSkill: _ClassVar[ETalentType]
    TalentType_Passive: _ClassVar[ETalentType]
TalentType_None: ETalentType
TalentType_Active: ETalentType
TalentType_SmallSkill: ETalentType
TalentType_Passive: ETalentType
