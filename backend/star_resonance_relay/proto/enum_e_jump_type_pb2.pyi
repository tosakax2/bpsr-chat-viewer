from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EJumpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EDefault: _ClassVar[EJumpType]
    EReverse: _ClassVar[EJumpType]
    EFallen: _ClassVar[EJumpType]
    EShimmy: _ClassVar[EJumpType]
    EKickWall: _ClassVar[EJumpType]
    EFive: _ClassVar[EJumpType]
    EPedalWallEnd: _ClassVar[EJumpType]
    EPedalWallStop: _ClassVar[EJumpType]
    ELazyJump: _ClassVar[EJumpType]
    EPedalWallOver: _ClassVar[EJumpType]
    ERideJump: _ClassVar[EJumpType]
    EBounceJump: _ClassVar[EJumpType]
EDefault: EJumpType
EReverse: EJumpType
EFallen: EJumpType
EShimmy: EJumpType
EKickWall: EJumpType
EFive: EJumpType
EPedalWallEnd: EJumpType
EPedalWallStop: EJumpType
ELazyJump: EJumpType
EPedalWallOver: EJumpType
ERideJump: EJumpType
EBounceJump: EJumpType
