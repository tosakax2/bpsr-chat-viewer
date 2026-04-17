from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ETimerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TimerTypeNull: _ClassVar[ETimerType]
    TimerType_Point: _ClassVar[ETimerType]
    TimerType_Day: _ClassVar[ETimerType]
    TimerType_Month: _ClassVar[ETimerType]
    TimerType_Week: _ClassVar[ETimerType]
    TimerType_Interval: _ClassVar[ETimerType]
TimerTypeNull: ETimerType
TimerType_Point: ETimerType
TimerType_Day: ETimerType
TimerType_Month: ETimerType
TimerType_Week: ETimerType
TimerType_Interval: ETimerType
