from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EClimbType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ClimbIdle: _ClassVar[EClimbType]
    Climbing: _ClassVar[EClimbType]
    ClimbRush: _ClassVar[EClimbType]
    ShinIdle: _ClassVar[EClimbType]
    Shining: _ClassVar[EClimbType]
    ShinCross: _ClassVar[EClimbType]
    TopBraceUp: _ClassVar[EClimbType]
    TopBraceDown: _ClassVar[EClimbType]
    BottomBraceUp: _ClassVar[EClimbType]
    BottomBraceDown: _ClassVar[EClimbType]
ClimbIdle: EClimbType
Climbing: EClimbType
ClimbRush: EClimbType
ShinIdle: EClimbType
Shining: EClimbType
ShinCross: EClimbType
TopBraceUp: EClimbType
TopBraceDown: EClimbType
BottomBraceUp: EClimbType
BottomBraceDown: EClimbType
