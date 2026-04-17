from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ETeamMemberChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ChangeTypeNull: _ClassVar[ETeamMemberChangeType]
    ChangeTypeJoin: _ClassVar[ETeamMemberChangeType]
    ChangeTypeLeave: _ClassVar[ETeamMemberChangeType]
    ChangeTypeLeader: _ClassVar[ETeamMemberChangeType]
    ChangeTypeRefuseLeader: _ClassVar[ETeamMemberChangeType]
ChangeTypeNull: ETeamMemberChangeType
ChangeTypeJoin: ETeamMemberChangeType
ChangeTypeLeave: ETeamMemberChangeType
ChangeTypeLeader: ETeamMemberChangeType
ChangeTypeRefuseLeader: ETeamMemberChangeType
