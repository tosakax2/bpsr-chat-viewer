from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ETrialRoadAwardState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TrialRoadAwardStateNone: _ClassVar[ETrialRoadAwardState]
    TrialRoadAwardStateFinish: _ClassVar[ETrialRoadAwardState]
    TrialRoadAwardStateGet: _ClassVar[ETrialRoadAwardState]
TrialRoadAwardStateNone: ETrialRoadAwardState
TrialRoadAwardStateFinish: ETrialRoadAwardState
TrialRoadAwardStateGet: ETrialRoadAwardState
