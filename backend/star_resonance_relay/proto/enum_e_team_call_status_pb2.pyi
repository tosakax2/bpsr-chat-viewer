from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ETeamCallStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ETeamCallStatus_Null: _ClassVar[ETeamCallStatus]
    ETeamCallStatus_Wait: _ClassVar[ETeamCallStatus]
    ETeamCallStatus_Agree: _ClassVar[ETeamCallStatus]
    ETeamCallStatus_Refuse: _ClassVar[ETeamCallStatus]
ETeamCallStatus_Null: ETeamCallStatus
ETeamCallStatus_Wait: ETeamCallStatus
ETeamCallStatus_Agree: ETeamCallStatus
ETeamCallStatus_Refuse: ETeamCallStatus
