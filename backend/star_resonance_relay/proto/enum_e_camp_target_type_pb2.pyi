from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ECampTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ECampSelf: _ClassVar[ECampTargetType]
    ECampEnemy: _ClassVar[ECampTargetType]
    ECampNeutral: _ClassVar[ECampTargetType]
    ECampFriendly: _ClassVar[ECampTargetType]
    ECampTeam: _ClassVar[ECampTargetType]
    ECampAll: _ClassVar[ECampTargetType]
ECampSelf: ECampTargetType
ECampEnemy: ECampTargetType
ECampNeutral: ECampTargetType
ECampFriendly: ECampTargetType
ECampTeam: ECampTargetType
ECampAll: ECampTargetType
