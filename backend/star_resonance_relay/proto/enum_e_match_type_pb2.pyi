from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EMatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMatchTypeNull: _ClassVar[EMatchType]
    EMatchTypeTeam: _ClassVar[EMatchType]
    EMatchTypeActivity: _ClassVar[EMatchType]
EMatchTypeNull: EMatchType
EMatchTypeTeam: EMatchType
EMatchTypeActivity: EMatchType
