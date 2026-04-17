from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EEnumVisitorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumVisitNone: _ClassVar[EEnumVisitorType]
    EnumVisitOwner: _ClassVar[EEnumVisitorType]
    EnumVisitCohabitant: _ClassVar[EEnumVisitorType]
    EnumVisitOther: _ClassVar[EEnumVisitorType]
EnumVisitNone: EEnumVisitorType
EnumVisitOwner: EEnumVisitorType
EnumVisitCohabitant: EEnumVisitorType
EnumVisitOther: EEnumVisitorType
