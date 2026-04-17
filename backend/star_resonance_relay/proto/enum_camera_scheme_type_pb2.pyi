from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CameraSchemeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DefaultScheme: _ClassVar[CameraSchemeType]
    CustomScheme: _ClassVar[CameraSchemeType]
DefaultScheme: CameraSchemeType
CustomScheme: CameraSchemeType
