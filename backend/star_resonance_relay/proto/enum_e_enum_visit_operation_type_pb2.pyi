from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EEnumVisitOperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumVisitOperNone: _ClassVar[EEnumVisitOperationType]
    EnumVisitOperEnter: _ClassVar[EEnumVisitOperationType]
    EnumVisitOperLevev: _ClassVar[EEnumVisitOperationType]
    EnumVisitOperKickOut: _ClassVar[EEnumVisitOperationType]
EnumVisitOperNone: EEnumVisitOperationType
EnumVisitOperEnter: EEnumVisitOperationType
EnumVisitOperLevev: EEnumVisitOperationType
EnumVisitOperKickOut: EEnumVisitOperationType
