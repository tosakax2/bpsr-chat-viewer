from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BuildFurnitureOpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BuildFurnitureOpAdd: _ClassVar[BuildFurnitureOpType]
    BuildFurnitureOpUpdate: _ClassVar[BuildFurnitureOpType]
    BuildFurnitureOpDelete: _ClassVar[BuildFurnitureOpType]
BuildFurnitureOpAdd: BuildFurnitureOpType
BuildFurnitureOpUpdate: BuildFurnitureOpType
BuildFurnitureOpDelete: BuildFurnitureOpType
