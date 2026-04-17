from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EEnumStructureSubType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumStructureSubTypeNone: _ClassVar[EEnumStructureSubType]
    EnumStructureSubTypeFloorMat: _ClassVar[EEnumStructureSubType]
    EnumStructureSubTypeWallMat: _ClassVar[EEnumStructureSubType]
EnumStructureSubTypeNone: EEnumStructureSubType
EnumStructureSubTypeFloorMat: EEnumStructureSubType
EnumStructureSubTypeWallMat: EEnumStructureSubType
