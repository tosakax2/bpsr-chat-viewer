from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ERotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RotNone: _ClassVar[ERotType]
    RotCurve: _ClassVar[ERotType]
    RotSpeed: _ClassVar[ERotType]
RotNone: ERotType
RotCurve: ERotType
RotSpeed: ERotType
