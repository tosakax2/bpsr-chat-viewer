from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EDungeonState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DungeonStateNull: _ClassVar[EDungeonState]
    DungeonStateActive: _ClassVar[EDungeonState]
    DungeonStateReady: _ClassVar[EDungeonState]
    DungeonStatePlaying: _ClassVar[EDungeonState]
    DungeonStateEnd: _ClassVar[EDungeonState]
    DungeonStateSettlement: _ClassVar[EDungeonState]
    DungeonStateVote: _ClassVar[EDungeonState]
DungeonStateNull: EDungeonState
DungeonStateActive: EDungeonState
DungeonStateReady: EDungeonState
DungeonStatePlaying: EDungeonState
DungeonStateEnd: EDungeonState
DungeonStateSettlement: EDungeonState
DungeonStateVote: EDungeonState
