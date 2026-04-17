from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EDungeonTimerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DungeonTimerTypeNull: _ClassVar[EDungeonTimerType]
    DungeonTimerTypeRightCommon: _ClassVar[EDungeonTimerType]
    DungeonTimerTypeMiddlerCommon: _ClassVar[EDungeonTimerType]
    DungeonTimerTypeHero: _ClassVar[EDungeonTimerType]
    DungeonTimerTypeWait: _ClassVar[EDungeonTimerType]
    DungeonTimerTypePrepare: _ClassVar[EDungeonTimerType]
DungeonTimerTypeNull: EDungeonTimerType
DungeonTimerTypeRightCommon: EDungeonTimerType
DungeonTimerTypeMiddlerCommon: EDungeonTimerType
DungeonTimerTypeHero: EDungeonTimerType
DungeonTimerTypeWait: EDungeonTimerType
DungeonTimerTypePrepare: EDungeonTimerType
