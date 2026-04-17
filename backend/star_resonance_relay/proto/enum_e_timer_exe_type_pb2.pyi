from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ETimerExeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TimerExeTypeNull: _ClassVar[ETimerExeType]
    TimerExeType_Start: _ClassVar[ETimerExeType]
    TimerExeType_End: _ClassVar[ETimerExeType]
    TimerExeType_Cycle_Start: _ClassVar[ETimerExeType]
    TimerExeType_Cycle_End: _ClassVar[ETimerExeType]
TimerExeTypeNull: ETimerExeType
TimerExeType_Start: ETimerExeType
TimerExeType_End: ETimerExeType
TimerExeType_Cycle_Start: ETimerExeType
TimerExeType_Cycle_End: ETimerExeType
