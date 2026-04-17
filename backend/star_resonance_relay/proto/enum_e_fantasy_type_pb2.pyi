from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EFantasyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EFantasyType_None: _ClassVar[EFantasyType]
    EFantasyType_Attack: _ClassVar[EFantasyType]
    EFantasyType_Auxiliary: _ClassVar[EFantasyType]
    EFantasyType_Defense: _ClassVar[EFantasyType]
    EFantasyType_Universal: _ClassVar[EFantasyType]
EFantasyType_None: EFantasyType
EFantasyType_Attack: EFantasyType
EFantasyType_Auxiliary: EFantasyType
EFantasyType_Defense: EFantasyType
EFantasyType_Universal: EFantasyType
