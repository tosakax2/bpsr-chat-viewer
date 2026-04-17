from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class StructureOpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    StructureOpTypeAdd: _ClassVar[StructureOpType]
    StructureOpTypeUpdate: _ClassVar[StructureOpType]
    StructureOpTypeDelete: _ClassVar[StructureOpType]
StructureOpTypeAdd: StructureOpType
StructureOpTypeUpdate: StructureOpType
StructureOpTypeDelete: StructureOpType
