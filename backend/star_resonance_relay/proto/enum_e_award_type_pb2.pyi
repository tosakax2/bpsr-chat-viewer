from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EAwardType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EAwardTypeNull: _ClassVar[EAwardType]
    EAwardTypeBdMod: _ClassVar[EAwardType]
    EAwardTypeSelect: _ClassVar[EAwardType]
EAwardTypeNull: EAwardType
EAwardTypeBdMod: EAwardType
EAwardTypeSelect: EAwardType
