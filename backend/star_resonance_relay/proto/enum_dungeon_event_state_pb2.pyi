from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonEventState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DungeonEventStateNull: _ClassVar[DungeonEventState]
    DungeonEventStateRunning: _ClassVar[DungeonEventState]
    DungeonEventStateEnd: _ClassVar[DungeonEventState]
DungeonEventStateNull: DungeonEventState
DungeonEventStateRunning: DungeonEventState
DungeonEventStateEnd: DungeonEventState
