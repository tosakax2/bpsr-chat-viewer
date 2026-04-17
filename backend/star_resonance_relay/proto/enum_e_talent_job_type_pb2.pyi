from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ETalentJobType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TalentJobType_None: _ClassVar[ETalentJobType]
    TalentJobType_Attack: _ClassVar[ETalentJobType]
    TalentJobType_Support: _ClassVar[ETalentJobType]
    TalentJobType_Survive: _ClassVar[ETalentJobType]
TalentJobType_None: ETalentJobType
TalentJobType_Attack: ETalentJobType
TalentJobType_Support: ETalentJobType
TalentJobType_Survive: ETalentJobType
