from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EMotionTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MotionTargetDefault: _ClassVar[EMotionTargetType]
    MotionTargetTargetPos: _ClassVar[EMotionTargetType]
    MotionTargetTargetPosFixed: _ClassVar[EMotionTargetType]
    MotionTargetTarget: _ClassVar[EMotionTargetType]
MotionTargetDefault: EMotionTargetType
MotionTargetTargetPos: EMotionTargetType
MotionTargetTargetPosFixed: EMotionTargetType
MotionTargetTarget: EMotionTargetType
