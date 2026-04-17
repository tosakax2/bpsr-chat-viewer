from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EBodySize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BodySizeNull: _ClassVar[EBodySize]
    BodySizeS: _ClassVar[EBodySize]
    BodySizeM: _ClassVar[EBodySize]
    BodySizeL: _ClassVar[EBodySize]
BodySizeNull: EBodySize
BodySizeS: EBodySize
BodySizeM: EBodySize
BodySizeL: EBodySize
