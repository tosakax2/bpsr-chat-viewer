from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EFightAttrInheritType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    InheritMaster: _ClassVar[EFightAttrInheritType]
    InheritCopyByMaster: _ClassVar[EFightAttrInheritType]
    NoInherit: _ClassVar[EFightAttrInheritType]
InheritMaster: EFightAttrInheritType
InheritCopyByMaster: EFightAttrInheritType
NoInherit: EFightAttrInheritType
