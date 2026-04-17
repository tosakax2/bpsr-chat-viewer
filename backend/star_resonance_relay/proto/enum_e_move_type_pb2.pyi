from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EMoveType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MoveIdle: _ClassVar[EMoveType]
    MoveWalk: _ClassVar[EMoveType]
    MoveRun: _ClassVar[EMoveType]
    MoveDash: _ClassVar[EMoveType]
    MoveDashEnd: _ClassVar[EMoveType]
    MoveAlert: _ClassVar[EMoveType]
    MoveFly: _ClassVar[EMoveType]
    MovePatrol: _ClassVar[EMoveType]
    MovePatrolRun: _ClassVar[EMoveType]
    MoveFlyDash: _ClassVar[EMoveType]
    MoveCustom: _ClassVar[EMoveType]
    MoveParkourRun: _ClassVar[EMoveType]
    MoveSelfPhoto: _ClassVar[EMoveType]
    MoveRotate: _ClassVar[EMoveType]
    MoveDashTurn: _ClassVar[EMoveType]
    MoveWalkEnd: _ClassVar[EMoveType]
    MoveRunEnd: _ClassVar[EMoveType]
    MoveWalkEndToIdle: _ClassVar[EMoveType]
    MoveRunEndToIdle: _ClassVar[EMoveType]
    MoveEightDir: _ClassVar[EMoveType]
    MoveByForce: _ClassVar[EMoveType]
    MoveSitRotate: _ClassVar[EMoveType]
    MoveJumpEndToIdle: _ClassVar[EMoveType]
MoveIdle: EMoveType
MoveWalk: EMoveType
MoveRun: EMoveType
MoveDash: EMoveType
MoveDashEnd: EMoveType
MoveAlert: EMoveType
MoveFly: EMoveType
MovePatrol: EMoveType
MovePatrolRun: EMoveType
MoveFlyDash: EMoveType
MoveCustom: EMoveType
MoveParkourRun: EMoveType
MoveSelfPhoto: EMoveType
MoveRotate: EMoveType
MoveDashTurn: EMoveType
MoveWalkEnd: EMoveType
MoveRunEnd: EMoveType
MoveWalkEndToIdle: EMoveType
MoveRunEndToIdle: EMoveType
MoveEightDir: EMoveType
MoveByForce: EMoveType
MoveSitRotate: EMoveType
MoveJumpEndToIdle: EMoveType
