from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ETeamActivityState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ETeamActivity_No: _ClassVar[ETeamActivityState]
    ETeamActivity_Start: _ClassVar[ETeamActivityState]
    ETeamActivity_Checking: _ClassVar[ETeamActivityState]
    ETeamActivity_Voting: _ClassVar[ETeamActivityState]
    ETeamActivity_Doing: _ClassVar[ETeamActivityState]
    ETeamActivity_End: _ClassVar[ETeamActivityState]
ETeamActivity_No: ETeamActivityState
ETeamActivity_Start: ETeamActivityState
ETeamActivity_Checking: ETeamActivityState
ETeamActivity_Voting: ETeamActivityState
ETeamActivity_Doing: ETeamActivityState
ETeamActivity_End: ETeamActivityState
