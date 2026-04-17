from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EPartDamageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ESingle: _ClassVar[EPartDamageType]
    EMulti: _ClassVar[EPartDamageType]
ESingle: EPartDamageType
EMulti: EPartDamageType
