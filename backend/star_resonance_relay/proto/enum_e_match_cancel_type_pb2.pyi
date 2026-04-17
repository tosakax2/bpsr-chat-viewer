from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EMatchCancelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EMatchCancelTypeNull: _ClassVar[EMatchCancelType]
    EMatchCancelTypeRequest: _ClassVar[EMatchCancelType]
    EMatchCancelTypeTimeout: _ClassVar[EMatchCancelType]
    EMatchCancelTypeUnReady: _ClassVar[EMatchCancelType]
    EMatchCancelTypeTeamMemberJoin: _ClassVar[EMatchCancelType]
    EMatchCancelTypeTeamMemberLeave: _ClassVar[EMatchCancelType]
    EMatchCancelTypeEnterDungeon: _ClassVar[EMatchCancelType]
EMatchCancelTypeNull: EMatchCancelType
EMatchCancelTypeRequest: EMatchCancelType
EMatchCancelTypeTimeout: EMatchCancelType
EMatchCancelTypeUnReady: EMatchCancelType
EMatchCancelTypeTeamMemberJoin: EMatchCancelType
EMatchCancelTypeTeamMemberLeave: EMatchCancelType
EMatchCancelTypeEnterDungeon: EMatchCancelType
