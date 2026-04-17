from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EBehitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BehitNormal: _ClassVar[EBehitType]
    BehitStiff: _ClassVar[EBehitType]
    BehitStiffBack: _ClassVar[EBehitType]
    BehitStiffDown: _ClassVar[EBehitType]
    BehitStiffAir: _ClassVar[EBehitType]
    BehitStiffFall: _ClassVar[EBehitType]
    BehitStiffFlow: _ClassVar[EBehitType]
    BehitStiffAction: _ClassVar[EBehitType]
    BehitStiffThrowMove: _ClassVar[EBehitType]
    BehitStiffThrowEnd: _ClassVar[EBehitType]
    BehitStiffBackBlocked: _ClassVar[EBehitType]
BehitNormal: EBehitType
BehitStiff: EBehitType
BehitStiffBack: EBehitType
BehitStiffDown: EBehitType
BehitStiffAir: EBehitType
BehitStiffFall: EBehitType
BehitStiffFlow: EBehitType
BehitStiffAction: EBehitType
BehitStiffThrowMove: EBehitType
BehitStiffThrowEnd: EBehitType
BehitStiffBackBlocked: EBehitType
