from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EBuildFurnitureState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BuildFurnitureStateNone: _ClassVar[EBuildFurnitureState]
    BuildFurnitureStateBuilding: _ClassVar[EBuildFurnitureState]
    BuildFurnitureStateSuccess: _ClassVar[EBuildFurnitureState]
BuildFurnitureStateNone: EBuildFurnitureState
BuildFurnitureStateBuilding: EBuildFurnitureState
BuildFurnitureStateSuccess: EBuildFurnitureState
