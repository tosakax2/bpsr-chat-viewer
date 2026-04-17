from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BodyPartType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BodyPartTypeDefault: _ClassVar[BodyPartType]
    BodyPartTypePart: _ClassVar[BodyPartType]
    BodyPartTypeMod: _ClassVar[BodyPartType]
BodyPartTypeDefault: BodyPartType
BodyPartTypePart: BodyPartType
BodyPartTypeMod: BodyPartType
