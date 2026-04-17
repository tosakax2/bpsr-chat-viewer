from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ETeamVoteRet(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ETeamVoteRetNull: _ClassVar[ETeamVoteRet]
    ETeamVoteRetAgree: _ClassVar[ETeamVoteRet]
    ETeamVoteRetRefuse: _ClassVar[ETeamVoteRet]
    ETeamVoteRetCancel: _ClassVar[ETeamVoteRet]
    ETeamVoteRetTimeOut: _ClassVar[ETeamVoteRet]
ETeamVoteRetNull: ETeamVoteRet
ETeamVoteRetAgree: ETeamVoteRet
ETeamVoteRetRefuse: ETeamVoteRet
ETeamVoteRetCancel: ETeamVoteRet
ETeamVoteRetTimeOut: ETeamVoteRet
