from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EMotionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MotionNone: _ClassVar[EMotionType]
    MotionCurve: _ClassVar[EMotionType]
    MotionSpeed: _ClassVar[EMotionType]
    MotionControl: _ClassVar[EMotionType]
MotionNone: EMotionType
MotionCurve: EMotionType
MotionSpeed: EMotionType
MotionControl: EMotionType
