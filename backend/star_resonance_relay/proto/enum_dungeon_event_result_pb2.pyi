from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonEventResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DungeonEventResultNull: _ClassVar[DungeonEventResult]
    DungeonEventResultSuccess: _ClassVar[DungeonEventResult]
    DungeonEventResultTimeOut: _ClassVar[DungeonEventResult]
    DungeonEventResultFailed: _ClassVar[DungeonEventResult]
    DungeonEventResultEnd: _ClassVar[DungeonEventResult]
DungeonEventResultNull: DungeonEventResult
DungeonEventResultSuccess: DungeonEventResult
DungeonEventResultTimeOut: DungeonEventResult
DungeonEventResultFailed: DungeonEventResult
DungeonEventResultEnd: DungeonEventResult
