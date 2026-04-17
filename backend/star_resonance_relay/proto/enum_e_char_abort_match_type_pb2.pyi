from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ECharAbortMatchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ECharAbortMatch_Void: _ClassVar[ECharAbortMatchType]
    ECharAbortMatch_CreateTeam: _ClassVar[ECharAbortMatchType]
    ECharAbortMatch_JoinTeam: _ClassVar[ECharAbortMatchType]
    ECharAbortMatch_Error: _ClassVar[ECharAbortMatchType]
ECharAbortMatch_Void: ECharAbortMatchType
ECharAbortMatch_CreateTeam: ECharAbortMatchType
ECharAbortMatch_JoinTeam: ECharAbortMatchType
ECharAbortMatch_Error: ECharAbortMatchType
