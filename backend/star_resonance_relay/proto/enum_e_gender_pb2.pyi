from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EGender(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GenderNull: _ClassVar[EGender]
    GenderMale: _ClassVar[EGender]
    GenderFemale: _ClassVar[EGender]
GenderNull: EGender
GenderMale: EGender
GenderFemale: EGender
