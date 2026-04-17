from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CameraPatternType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Default: _ClassVar[CameraPatternType]
    SelfPhoto: _ClassVar[CameraPatternType]
    AR: _ClassVar[CameraPatternType]
Default: CameraPatternType
SelfPhoto: CameraPatternType
AR: CameraPatternType
