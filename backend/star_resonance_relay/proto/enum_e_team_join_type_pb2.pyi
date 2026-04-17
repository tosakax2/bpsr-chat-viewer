from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ETeamJoinType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ETeamJoinTypeNone: _ClassVar[ETeamJoinType]
    ETeamJoinTypeInvite: _ClassVar[ETeamJoinType]
    ETeamJoinTypeTargetMatch: _ClassVar[ETeamJoinType]
ETeamJoinTypeNone: ETeamJoinType
ETeamJoinTypeInvite: ETeamJoinType
ETeamJoinTypeTargetMatch: ETeamJoinType
